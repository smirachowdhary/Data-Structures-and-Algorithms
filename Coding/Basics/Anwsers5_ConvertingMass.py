# Program gets a mass from the user and converts the mass to various other measurement forms.
mass_in_pounds = int(input("Please give me a mass in pound. Enter here:"))

print(f"Your mass is... 
{mass_in_pounds} pounds, 
{mass_in_pounds * 16} ounces, 
{mass_in_pounds / 2.205} kilogram, 
and {mass_in_pounds * 454} gram.")