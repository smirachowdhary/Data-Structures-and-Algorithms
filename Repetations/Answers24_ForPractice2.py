n = int(input("Enter a number:"))

for i in range(n):
    j=i+1
    print("*"*j)
print("")
for i in range(n):
    j=i+1
    print("*"*(2*i+1))
print("")
for i in range(n):
    j=i+1
    print("*"*(n-i))
print("")
for i in range(n):
    j = 2*(n-i)
    y = 1*(j-1)
    print("*"*y)