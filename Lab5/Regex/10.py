import re

txt = input()

x = re.sub(r"([A-Z][a-z]*)" , r"\1_" , txt)
y = re.sub("([A-Z])" , lambda x : x.group(1).lower() , x)
y = y[:-1]

print(y)
