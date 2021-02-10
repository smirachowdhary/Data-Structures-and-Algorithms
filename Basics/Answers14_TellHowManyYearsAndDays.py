import datetime
from datetime import date

year = int(input("""Give me the year you were born in(numbers only):"""))
month = int(input("""Give me the month you were born in(numbers only):"""))
day = int(input("""Give me the day you were born in(numbers only):"""))
d1 = datetime.datetime(year,month,day)
today = datetime.datetime.now()
today_year = datetime.date.today().year
print(f"""
You've have lived {today_year - year} years.
You've have lived {today - d1} days.
""")