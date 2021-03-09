n = int(input("Enter number:"))
print(f"The prime numbers till {n} are:")

i=2
while i < n:
    end = i//2
    j=2
    while j <= end:
        if i % j == 0:
            break
        j+=1
    else:
        print(i, end=" ")
    i+=1