nos = int(input("Number of students:"))
students = []

i = 0
while i < nos:
    user_name = input("Enter name:")
    eng = int(input("Enter English Marks out of 10:"))
    sci = int(input("Enter Science Marks out of 10:"))
    math = int(input("Enter Math Marks out of 10:"))
    average = (eng + sci + math) / 3
    temp=[]
    temp.append(user_name)
    temp.append(eng)
    temp.append(sci)
    temp.append(math)
    temp.append(average)
    students.append(temp)
    print(f"""
    Student name: {students[i][0]}
    English Marks: {students[i][1]}
    Science Marks: {students[i][2]}
    Math Marks: {students[i][3]}
    Average: {students[i][4]:5.2f}
    """)
    i+=1

# print(len(students))
# print(students)