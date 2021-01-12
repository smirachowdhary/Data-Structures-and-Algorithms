import random
#This makes me able to get stuff randomly.
n1 = random.randint(1,20)
n2 = random.randint(100,1000)
#This makes to varibles for the question and the varibles are random in that varible.
print (f"{n1} * {n2}")
answer = int(input(""))
#This is giving the user a question and recording her/his answer.
if n1 * n2 == answer:
    print ("Great Job! Your answer is correct.")
else:
    print(f"Sorry, you answer is not correct. The real answer is {n1 * n2}.")
#This is checking wether the answer is correct or incorrect and giving a fitting reply.
n2 = random.randint(1,20)
n1 = random.randint(100,1000)
#This makes to varibles for the question and the varibles are random in that varible.
print (f"{n1} / {n2}")
answer = int(input(""))
#This is giving the user a question and recording her/his answer.
if n1 / n2 == answer:
    print ("Great Job! Your answer is correct.")
else:
    print(f"Sorry, you answer is not correct. The real answer is {n1 / n2}.")
#This is checking wether the answer is correct or incorrect and giving a fitting reply.