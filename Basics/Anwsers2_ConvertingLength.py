# Program gets a length from the user and converts the length to various other measurement forms.
length_in_miles = int(input("Please give me a length in miles. Enter here:"))

print(f"""Your length is 
{length_in_miles} miles, 
{length_in_miles * 63360} inch, 
{length_in_miles * 5280} feet, 
{length_in_miles * 1760} yard, 
{length_in_miles * 1.60934} kilometers, 
{length_in_miles * 1609.34} meters, and 
{length_in_miles * 160934} centimeters.""")