# SETS

import re

# Example 4.1 : Check if the string has any a, r, or n characters:
txt = "The rain in Spain"
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Example 4.2 :Check if the string has any characters between a and n:
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.3 : #Check if the string has other characters than a, r, or n:
txt = "The rain in Spain"
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.4 : Check if the string has any 0, 1, 2, or 3 digits:
txt = "The rain in Spain"
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.5 : check if the string has any digits:
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.6 : Check if the string has any two-digit numbers, from 00 to 59
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.7 : Check if the string has any characters from a to z lower case, and A to Z upper case:
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Example 4.8: Check if the string has any + characters:
txt = "8 times before 11:45 + AM"
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



