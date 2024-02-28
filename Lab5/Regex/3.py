import re

txt = input()
y = txt.split(" ")

for i in y :
    x = re.findall("^[a-z][a-z]*_[a-z]*$" , i) 
    if x:
        print(x)