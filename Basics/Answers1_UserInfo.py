# Program gets user data like name, age, height & weight.
# It provides formatted information with height and weight in various measurment units
first_name = input("What is your first name?")
last_name = input("What is your last name?")
age_in_years = float(input("What is your age in years?"))
height_in_feet = float(input("How tall are you (in feet)?"))
weight_in_pounds = float(input("How much do you weigh (in pounds)?"))

print(f""" 
Good day, {first_name.upper()} {last_name.upper()}!!
You have lived at least {age_in_years:2.0f} years, {age_in_years * 12:2.0f} months, {age_in_years * 52.1429:5.0f} weeks, or {age_in_years * 365:2.0f} days.
Your height is {height_in_feet} feet, {height_in_feet * 12:5.3f} inches, or {height_in_feet * 30.48:5.3f} centimeters.
Your weight is {weight_in_pounds:5.2f} pounds or {weight_in_pounds / 2.205:5.4f} kilograms.
Nice to meet you. Bye!
""")