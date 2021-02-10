# Program gets a money value from the user and converts the money to various other measurement forms.
money_value = float(input("Enter a money value here in dollars:"))
half_dallors = money_value // 0.50
quarters = money_value % 0.50 // 0.25
dimes = money_value % 0.50 % 0.25 // 0.10
nickels = money_value % 0.50 % 0.25 % 0.10 // 0.05
pennies = money_value % 0.50 % 0.25 % 0.10 % 0.05 // 0.01

print(f" You have... 
{half_dallors} half dallors, 
{quarters} quarters, 
{dimes} dimes, 
{nickels} nickels, 
and {pennies} pennies.")