import random

def maximum(a, b, c):
    maxi = a
    if a < b:
        maxi = b
        if b < c:
            maxi = c
            print(f"The max of the 3 numbers is {maxi}.")
        elif b > c:
            print(f"The max of the 3 numbers is {maxi}.")
    elif a < c:
        maxi = c
        print(f"The max of the 3 numbers is {maxi}.")
    elif a > c:
        print(f"The max of the 3 numbers is {maxi}.")
    elif a == b == c:
        print("All your numbers are equal to each other.")

n1_from_user = int(input("Enter a number:"))
n2_from_user = int(input("Enter a number:"))
n3_from_user = int(input("Enter a number:"))
def_from_user = maximum(n1_from_user, n2_from_user, n3_from_user)

n1_from_random = random.randint(0,1000)
n2_from_random = random.randint(0,1000)
n3_from_random = random.randint(0,1000)
def_from_random = maximum(n1_from_random, n2_from_random, n3_from_random)