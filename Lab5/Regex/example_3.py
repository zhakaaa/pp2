#SPECIAL SEQUENCES

import re

#Example 3.1 : check if the string started with 'The'
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")


# Example 3.2 : check if 'ain' presented at the begining of word
txt = "The rain in Spain"

x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# check if 'ain' presented  at the end of word
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Example 3.3 : check if the 'ain' presented in string , BUT NOT AT THE BEGINNING
txt = "The rain in Spain"

x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# check if the 'ain' presented in string , BUT NOT AT THE END
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Example 3.4 : check if the string contain any digit
txt = "The rain in Spain"
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# check if the string DON'T containn any digit
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 3.5 : check if the string contain white-space. return matches at every white-space characters
txt = "The rain in Spain"

x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# check if string DON'T contain white-space. return matches at every NON white-space characters
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 3.6 : Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
txt = "The rain in Spain"

x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 3.7 : Check if the string ends with "Spain"e
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")








