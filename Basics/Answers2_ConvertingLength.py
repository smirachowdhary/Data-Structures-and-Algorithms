# Program gets a length from the user and converts the length to various other measurement forms.
length_in_miles = int(input("Please give me a length in miles. Enter here:"))

print(f"""Your length is 
{length_in_miles} miles, 
{length_in_miles * 63360:10.3f} inch, 
{length_in_miles * 5280:10.3f} feet, 
{length_in_miles * 1760:10.3f} yard, 
{length_in_miles * 1.60934:10.3f} kilometers, 
{length_in_miles * 1609.34:10.3f} meters, and 
{length_in_miles * 160934:10.3f} centimeters.""")