from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///chemicals.db")
chemicals = db.execute("SELECT name, mw FROM chemicals ORDER BY name")
elements = db.execute("SELECT name, symbol, aw FROM elements ORDER BY id")
chemical_names = [chemical["name"] for chemical in chemicals]
symbols = db.execute("SELECT symbol FROM elements ORDER BY id")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        if 'buffer' in request.form:
            chemicals = db.execute("SELECT name, mw FROM chemicals ORDER BY name")
            chemical_names = [chemical["name"] for chemical in chemicals]
            return render_template("buffer.html", chemicals=chemical_names)
        elif 'table' in request.form:
            return render_template("ptable.html", elements=elements)
        elif 'weight' in request.form:
            return render_template("weight.html", symbols=symbols)

@app.route("/input", methods=["GET", "POST"])
def add():
    global chemicals

    if request.method == "GET":
        return render_template("input.html")

    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            return render_template("error.html", code="400", message="User did not insert a valid chemical name.")
        for chemical in chemicals:
            if name == chemical["name"]:
                return render_template("error.html", code="400", message="Chemical name already exists in selection.")
        try:
            mw = float(request.form.get("mw"))
        except ValueError:
            return render_template("error.html", code="500", message="Value Error.")
        if not mw:
            return render_template("error.html", code="400", message="User did not insert a valid molecular weight (mw).")
        if mw < 1:
            return render_template("error.html", code="400", message="User did not insert a valid molecular weight (mw).")

        db.execute("INSERT INTO chemicals (name, mw) VALUES (?, ?)", name, mw)
        chemicals = db.execute("SELECT name, mw FROM chemicals ORDER BY name")
        chemical_names = [chemical["name"] for chemical in chemicals]
        return render_template("buffer.html", chemicals=chemical_names)

@app.route("/buffer", methods=["GET", "POST"])
def buffer():
    if request.method == "GET":
        chemicals = db.execute("SELECT name, mw FROM chemicals ORDER BY name")
        chemical_names = [chemical["name"] for chemical in chemicals]
        return render_template("buffer.html", chemicals=chemical_names)

    if request.method == "POST":
        chem_name = request.form.get("chemical")
        if not chem_name:
            return render_template("error.html", code="400", message="User did not insert a valid chemical name.")

        mol = request.form.get("mol")
        if not mol:
            return render_template("error.html", code="400", message="User did not insert a valid molarity (M).")

        vol = request.form.get("vol")
        if not vol:
            return render_template("error.html", code="400", message="User did not insert a valid volume (L).")

        mw = db.execute("SELECT mw FROM chemicals WHERE name = ?", chem_name)
        mw = mw[0]["mw"]

        try:
            vol = float(vol)
            mol = float(mol)
        except ValueError:
            return render_template("error.html", code="500", message="Value Error.")
        if mol <= 0:
            return render_template("error.html", code="400", message="User did not insert a valid molarity (M).")
        if vol <= 0:
            return render_template("error.html", code="400", message="User did not insert a valid volume (L).")

        weight = (mw * mol) * vol
        weight = format(weight, '.3f')

        return render_template("calculated.html", weight=weight, vol=vol, chemical=chem_name, mol=mol)

@app.route("/ptable")
def table():
        elements = db.execute("SELECT * FROM elements")
        return render_template("ptable.html", elements=elements)

@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "GET":
        return render_template("weight.html", symbols=symbols)

    if request.method == "POST":
        mw = 0
        formuladict = {}
        inputs = []

        key = request.form.getlist("formula")
        if not all(key):
            return render_template("error.html", code="400", message="User did not insert any/all elements that were required")

        value = request.form.getlist("amount")
        if not all(value):
            return render_template("error.html", code="400", message="User did not insert any/all amounts that were required.")

        for i in range(len(key)):
            formuladict[key[i]] = value[i]

        for key, value in formuladict.items():
            for element in elements:
                if key == element["symbol"]:
                    inputs.append(key)
                    atomic_weight = element["aw"]
                    mw += float(atomic_weight) * float(value)
                    if int(value) > 1:
                        inputs.append(value)

        formula = ''.join(map(str, inputs))

        return render_template("calweight.html", formula=formula, mw=mw)
