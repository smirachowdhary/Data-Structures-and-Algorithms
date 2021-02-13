# Program gets a length from the user and converts the time to various other measurement forms.
time_in_days = int(input("Please give me a time in days. Enter here:"))

print(f"""Your time is... 
{time_in_days} days, 
{time_in_days * 1440:10.3f} minutes, 
{time_in_days * 24:10.3f} hours, 
{time_in_days * 86400:10.3f} seconds, 
and {time_in_days / 7:10.3f} weeks.""")