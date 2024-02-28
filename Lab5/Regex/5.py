import re

txt = input()
y = txt.split(" ")

for i in y :
    x = re.findall(".*a.*b$",i)
    if x :
        print(x)
        