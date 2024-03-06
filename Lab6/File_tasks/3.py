import os

path = input()

if os.path.exists(path) :
    print("Found")
    print("Filename: " ,os.path.basename(path))
    print("Directory name: " ,os.path.dirname(path))
else :
    print("Not Found")