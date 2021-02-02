import random

random_number1 = random.randint(100,1000)
random_number2 = random.randint(1,100)

print(f"{random_number1} * {random_number2}")
User_answer = int(input("Enter Answer(No commas or you'll get your question wrong):"))
if random_number1 * random_number2 == User_answer:
    print("You are correct!!")
else:
    print("Sorry, you are wrong. Try again(this is your last chance).")
    Last_chance = int(input("Enter Answer(No commas or you'll get your question wrong):"))
    if random_number1 * random_number2 == Last_chance:
        print("You are correct!!")
    else:
        print(f"Sorry, you are wrong. The real answer is {random_number1 * random_number2}.")