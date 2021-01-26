# Program gets user data like name, age, height & weight.
# It provides formatted information with height and weight in various measurment units
last_name = input("What is your last name?")
age_in_years = int(input("What is your age in years?"))
height_in_feet = float(input("How tall are you (in feet)?"))
weight_in_pounds = float(input("How much do you weigh (in pounds)?"))

print(f""" 
Good day, {first_name} {last_name}!!
You have lived at least {age_in_years} years, {age_in_years * 12} months, {age_in_years * 52.1429} weeks, or {age_in_years * 365} days.
Your height is {height_in_feet} feet, {height_in_feet * 12} inches, or {height_in_feet * 30.48} centimeters.
Your weight is {weight_in_pounds} pounds or {weight_in_pounds / 2.205} kilograms.
Nice to meet you. Bye!
""")