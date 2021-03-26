import os

cwd = os.getcwd()
print(cwd)

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(__file__)

# os.chdir(dir_path)

# dir_path = "C:\\Smira\\GitHub\\PythonAnswers\\Examples\\Input"
file1 = dir_path + "\\test.txt"
dir1 = cwd + "\\data\\input"

os.makedirs(dir1)
os.chdir(dir1)

target = open("myfile.txt", "w")
target.write("I love my mom a lot!")

input("exit")