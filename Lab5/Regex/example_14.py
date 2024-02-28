import re

# return tuple with containing start and end position 
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# return string 
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# return string that start with "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

