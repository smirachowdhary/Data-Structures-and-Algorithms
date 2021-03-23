import os

print (os.getcwd())
file_name = "test_2021_03_23"
target = open(filePath + file_name + ".txt", "w+")
target.write("Hello file!!")
target.write("Line 2!!")
# change path: os.chdir(path)

# target = open(file_name + ".txt", "w+")
# print(target.read())
target = open(file_name + ".txt")
for line in target:
    print(line)


# print(target.readline())