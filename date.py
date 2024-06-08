from datetime import datetime

now = datetime.now()

date = now.date()
datestr = date.strftime('%d-%m-%Y')

print(f"Date: {datestr}")

time = now.time()
timestr = time.strftime('%H:%M:%S')
print(f"Time: {timestr}")
