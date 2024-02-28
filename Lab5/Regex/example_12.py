import re

#Replace the first two occurrences of a white-space character with the digit 9:
# we can control number of occurences

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
