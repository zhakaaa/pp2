import re

txt = input()
y = txt.split(" ")

for i in y :
    x = re.findall(".*abb|abbb.*" , i) 
    if x:
        print(x)