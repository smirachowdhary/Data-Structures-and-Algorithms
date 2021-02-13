n = int(input("Give me a number:"))
# Printing 1 to n
for i in range(n):
    print(i+1, end=" ")
print("\n")
# Printing 0 to n-1
for i in range(n):
    print(i, end=" ")
print("\n")
# Printing n-1 to 0
for i in range(n):
    print(n-(i+1), end=" ")
print("\n")
# Printing n to 1
for i in range(n):
    print(n-i, end=" ")
print("\n")
# Printing n odd numbers, starting from 1
for i in range(n):
    print(2*i+1, end=" ")
print("\n")
# Printing n even numbers, starting from 0
for i in range(n):
    print(2*i, end=" ")
print("\n")