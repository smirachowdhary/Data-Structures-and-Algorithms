import random

def maximum(n1, n2, n3)
    max = n1
    if n1 < n2:
        max = n2
        if n2 < n3:
            max = n3
            print(f"The max of the 3 numbers is {max}.")
        elif n2 > n3:
            print(f"The max of the 3 numbers is {max}.")
    elif n1 < n3:
        max = n3
        print(f"The max of the 3 numbers is {max}.")
    elif n1 > n3:
        print(f"The max of the 3 numbers is {max}.")
    elif n1 == n2 == n3:
        print("All your numbers are equal to each other.")

n1_from_user = int(input("Enter a number:"))
n2_from_user = int(input("Enter a number:"))
n3_from_user = int(input("Enter a number:"))
