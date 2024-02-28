import re

txt = "The spain AsafASaa AAsfd"
x = txt.split(" ")

for i in x :
    y = re.findall("[A-Z]{1}[a-z]*[a-z]$", i)
    if y :
        print(y)