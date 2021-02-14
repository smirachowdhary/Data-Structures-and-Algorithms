n = int(input("Give me a number:"))
# Printing 1 to n
i = 0
while i < n:
    print(i+1, end=" ")
    i+=1
print("\n")
# Printing 0 to n-1
i = 0
while i < n:
    print(i, end=" ")
    i+=1
print("\n")
# Printing n-1 to 0
i = n-1
while i >= 0:
    print(i, end=" ")
    i-=1
print("\n")
# Printing n to 1
i = n
while i > 0:
    print(i, end=" ")
    i-=1
print("\n")
# Printing n odd numbers, starting from 1
i = 0
while i < n:
    print(2*i+1, end=" ")
    i+=1
print("\n")
# Printing n even numbers, starting from 0
i = 0
while i < n:
    print(2*i, end=" ")
    i+=1