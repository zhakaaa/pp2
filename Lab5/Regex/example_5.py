import re

# return every occurences of "ai" e
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
