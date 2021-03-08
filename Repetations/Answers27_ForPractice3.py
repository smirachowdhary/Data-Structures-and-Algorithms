n = int(input("Enter number:"))
print(f"The prime numbers in {n} is:")

for i in range(2,n):
    end=i//2
    for j in range(2, end+1):
        if i%j == 0:
            break
    else:
        print(i, end=" ")