# Example 1.1 : Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)         # apple banana cherry


# Example 1.2 : Loop through the letters in the word "banana"
for x in "banana":
  print(x)    # b a n a n a


# Example 1.3 : Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)     # apple banana
  if x == "banana":
    break
  

# Example 1.4 : Exit the loop when x is "banana", but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)   # apple


# Example 1.5 : Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)    # apple cherry


# Example 1.6 : The "range()" method return a sequence of numbers started from 0 and increase by 1 (by default)
for x in range(6):
  print(x)    # 0 1 2 3 4 5 


# Example 1.7 : Started from 2 until 6
for x in range(2, 6):
  print(x)   # 2 3 4 5


# Example 1.8 : It is possible to specify the increment value by adding a third parameter
for x in range(2, 30, 3):
  print(x)     # 2 5 8 11 14 17 20 23 26 29 


# Example 1.9 :  Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")   # 0 1 2 3 4 5 Finally finished!


# Example 1.10 : If the loop breaks, the else block is not executed.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")   # 0 1 2


# Example 1.11 : A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  # red apple , red banana , red cherry , big apple , big banana , big cherry , tasty apple , tasty banana , tasty cherry


# Example 1.12 : For loops cannot be empty if for some reason you have empty for loop it will cause error without "pass" keyword
for x in [0, 1, 2]:
  pass 
 