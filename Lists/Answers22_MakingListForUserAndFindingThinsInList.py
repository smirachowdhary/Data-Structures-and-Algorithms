user_list = []
HMT = int(input("Enter how long you want your list to be here:"))

i = 0
while i < HMT:
    user_input = input("Input something:")
    user_list.append(user_input)
    i+=1

print("I shall print your list for you:")
print(user_list)
NFL = int(input(f"When I asked you to type something {HMT} times, which time do you want to konw now(enter number):"))
HMTHMT = int(input("And how many times?"))

i=0
while i < HMTHMT:
    print(user_list[NFL-1])
    i+=1

i = 0
while i < len(user_input):
    print(user_list[i].upper())
    i+=1

for item in user_list:
    print(user_list[i].upper())