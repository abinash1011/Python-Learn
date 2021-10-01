import datetime
date = datetime.datetime(2021, 9, 30)

if date > datetime.datetime.now():
    print("future")
elif date < datetime.datetime.now():
    print("past")
else:
    print("present")