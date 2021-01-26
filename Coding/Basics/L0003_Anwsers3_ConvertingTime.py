# Program gets a length from the user and converts the time to various other measurement forms.
time_in_days = int(input("Please give me a time in days. Enter here:"))

print(f"Your time is... 
{time_in_days} days, 
{time_in_days * 1440} minutes, 
{time_in_days * 24} hours, 
{time_in_days * 86400} seconds, 
and {time_in_days / 7} weeks.")