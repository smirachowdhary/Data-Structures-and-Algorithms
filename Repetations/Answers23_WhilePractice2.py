n = int(input("Enter a number:"))

i=0
while i < n:
    j=i+1
    print("*"*j)
    i+=1
print("")
i=0
while i < n:
    j=i+1
    print("*"*(2*i+1))
    i+=1
print("")
i=0
while n > i:
    j=i+1
    print("*"*(n-i))
    i+=1
print("")
i=0
while n > i:
    j = 2*(n-i)
    y = 1*(j-1)
    print("*"*y)
    i+=1