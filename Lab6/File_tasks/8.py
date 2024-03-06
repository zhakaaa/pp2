import os

file = input()

if os.path.exists(file) :
    print("This file is deleted")
    os.remove(file)
else :
    print("File not exist")