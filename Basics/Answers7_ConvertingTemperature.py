# Program gets a tempurture from the user and converts the tempurture to various other measurement forms.
tempurture_in_fahrenheit = int(input("Please give me a tempurture in fahrenheit. Enter here:"))

print(f"""Your tempurture in... 
{tempurture_in_fahrenheit} fahrenheit, 
{(tempurture_in_fahrenheit - 32) * 5/9} celius, 
and {(tempurture_in_fahrenheit - 32) * 5/9 + 273.15} Kelvin.""")