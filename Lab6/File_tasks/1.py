import os

print("All files: ")
for i in os.listdir() :
    if os.path.isfile(i) :
        print(i)

print("\n")
print("All files and directories: ")
for i in os.listdir() :
    if os.path.isdir(i) :
        print(i, "is directory")
    else :
        print(i , "is file")

print('\n')
for i in os.listdir(r'D:\Пользователи\Python\Lab6\Read_file'):
    print(i)

