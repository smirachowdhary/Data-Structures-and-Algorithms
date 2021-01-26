# Program gets a volume from the user and converts the volume to various other measurement forms.
volume_in_quarts = int(input("Please give me a volume in quarts. Enter here:"))

print(f"Your volume is... 
{volume_in_quarts} quarts, {volume_in_quarts * 3.943} cups, 
{volume_in_quarts * 946} mililiters, 
{volume_in_quarts / 1.057} liters, 
{volume_in_quarts * 2} pints, 
and {volume_in_quarts / 4} gallons.")