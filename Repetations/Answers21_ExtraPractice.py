student_info =[
    ["Smira","p"],
    ["Maya","p"],
    ["Jonathan","a"],
    ["Xavier","n"],
    ["Alisa","a"]
    ]


i=0
while i<5:
    print(f"{student_info[i][0]} is {student_info[i][1]}")
    i+=1


for item in student_info:
    print(f"{item[0]} is {item[1]}")