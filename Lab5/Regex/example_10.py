import re

# Split the string at the first white-space character:
# we can control number of occurences

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
