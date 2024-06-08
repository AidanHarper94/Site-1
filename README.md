Project created for CS50 course.

This is a contribution

# THE SCIENCE ZONE!
#### Video Demo: https://youtu.be/9soGtDgvc6s
#### Description:
Welcome to the Science Zone! As someone who has worked in the science sector before, i remembered how useful buffer calculators were online (Sigma Aldrich having the most popular one), but i found it painful if they didn't have the exact buffer you were looking for as you had to have one tab open for the periodic table, and a calculator/excel file to keep the sum of these elements you wanted. Hence why i have now built my very own buffer calculator that has functionality to add new buffer systems, a periodic table and molecular weight calculator.

The buffer calculator will input the buffer system selected, the molarity (strength) and volume required, and output a simple recipe for teh desired buffer. The periodic table is nothing more than just a table filled with a database of the elements, their symbols and their atomic weights, it's also slighty interactive with it zooming when you hover over the elements. Finally the molecular weight calculator takes the input(s) given by the user, such as element(s) and amount(s) and outputs the total molecular formula and weight.

I have used SQL, Python, HTML, CSS, Jinja, Flask and JavaScript within this project. The chemicals.db file consists of 2 tables of data, one called chemicals and the other called elements.

**The science zone consists of many HTML pages:**
- layout: Containing the layout and formatting for all pages, hosting the navigation banner and footer.
- index: This is the homepage. No login required as this would be a public system with no restricions on use.
- buffer: This is the page for the buffer form, allowing users to either calculate their buffer recipe or add a new buffer to the system.
- calculated: This is the output page for buffer, containing the buffer recipe.
- input: This is the page where users can add their own buffer system into the database.
- ptable: This is the page that hosts the periodic table populated from a database query, and an embedded YouTube video (that i hope you enjoy as much as i do).
- weight: This hosts the form for users to select their elements and add the amounts of each element. This also includes some JavaScript (from the help of ChatGPT) that has the append() function, that allows users to enter multiple elements and amounts.
- calweight: This renders the result of the molecular weight calculator page.
- error: This page just renders an error with a code and message to detail what went wrong (my hope is that this only shows if someone alters the HTML code in their session).

**Within app.py:**
- There are SQL queries that are used somewhat globally.
- route "/": This renders the homepage (GET) and sends the user to their selected app (POST).
- "/input": (GET) renders the page. (POST) ensures users have used the form correctly, and if so, inserts their inputs into the respected area in the database file.
- "/buffer": (GET) renders the page. (POST) ensures users have used the form correctly, then searches the molecular weight (mw) from the chemicals table, then uses the mw, volume and molarity to produce a weight (actual weight of chemical needed to produce buffer) and renders the calculated html with these inputs.
- "/ptable": Only has one method (GET) which simply uses a global database query and populates the periodic table using Jinja.
- "/weight": (GET) renders the page. (POST) creates a list and a dictionary, ensures the users have used the form correctly and stores the inputs in the dictionary. If the elements selected are in the database (which they should be as the dropdown menu is created from a database query), then the element is assign as a key, and the amount is a value. The element is also added onto the list and if the amount is above 1, then this is added onto the list. It finds the atomic weight of the element selected, multiplies that by the amount and keeps a running sum of this in mw. Finally it converts the list (formula) into a string so it can be rendered onto the calweight.html along with the final mw.

**My style choices:**

Although new to how to design a webpage/site, i found i learnt quite a bit and was happy with the final product. It's by no means perfect but i think it shows a bountiful amount of learning and skills. I designed the background myself (along with googling some icons) and went with a soft theme on the site in general.

**Support:**

Support mainly came from CS50.ai (God bless that duck!) for the coding, and CSS Selectors (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) for some stying options (i really liked that i could see the visual examples, both in code and on the page), but one question was asked to ChatGPT and that was around using JavaScript in order to create the clone and append onto the same form (as seen in weight.html).
