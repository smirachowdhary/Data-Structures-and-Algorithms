a = input("Enter something here:")
b = input("Enter something here:")

if len(a) > len(b):
    print (f"'{a}' has more charcters in its string.")
elif len(a) < len(b):
    print (f"'{b}' has more charcters in its string.")
else:
    print (f"'{a}' and '{b}' has equal charcters in its string.")

# OUTPUT:
# Enter something here:1234567890
# Enter something here:qwertyuiopasdfghjklzxcvvbnm
# 'qwertyuiopasdfghjklzxcvvbnm' has more charcters in its string.