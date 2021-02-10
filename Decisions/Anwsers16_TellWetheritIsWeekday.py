import datetime

day = int(input("Enter day:"))
month = int(input("Enter month:"))
year = int(input("Enter year:"))
date = datetime.datetime(year,month,day)

print(f"""
Your date is {month}\{day}\{year}
It is on the weekday(0-6 representing mon-sun): {d1.weekday()}
""")