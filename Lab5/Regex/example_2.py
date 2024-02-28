#METACHARACTERS

import re

#Example 2.1 : find all lowercase characters between "a" and "m"
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


#Example 2.2 : find all digits in txt
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)


#Example 2.3 : serch sequence that start with "he" and SPECIFIED NUMBER OF CHARACTERS and end with "o"
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)


#Example 2.4 : find string that starts with "hello"
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#Example 2.5 : fint string that ends with "planet"
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


#Example 2.6 : find string that starts with "he" and ZERO OR MORE NUMBER OF CHARACTERS and ends with "o"
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)


#Example 2.7 : find string that starts with "he" and ONE OR MORE NUMBER OF CHARACTER and ends with "o"
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)


#Example 2.8 : find string that starts with "he" and ZERO OR ONE NUMBER OF CHARACTER and ends with "o"
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)

#Exampla 2.9 : find string that starts with "he" and EXACTLY SPECIFIED NUMBER OF CHARACTERS and ends with "o"
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)


#Example 2.10 : find either "falls" or "stays" in string
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


