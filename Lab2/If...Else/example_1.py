# Example 1.1 :
a = 33
b = 200
if b > a:
  print("b is greater than a")  # b is greater than a


# Example 1.2 :
a = 33
b = 200

if b > a:
  print("b is greater than a")
#print("b is greater than a")  # error. if statement need identation


# Example 1.3 : Elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")    # a and b are equal


# Example 1.4 : Else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")   # a is greater than b



# Example 1.5 : We can use "else" without "elif"
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")     # b is not greater than a


# Example 1.6 : Short hand If statement
a = 200
b = 33

if a > b: print("a is greater than b")    # a is greater than b


# Example 1.7 : Short hand If...Else statement
a = 2
b = 330

print("A") if a > b else print("B")   # B


# Example 1.8 : Short hand If...Else statement
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")   # =


# Example 1.9 : The "and" kewyword is logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")   # Both conditions are True


# Example 1.10 : The "or" kewyword is logical operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")   # At least one of the conditions is True


# Example 1.11 : The "not" keyword is a logical operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")  # a is NOT greater than b


# Example 1.12 : If statement that contain another If statement is called - nested If statement
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")          #Above ten,
#                                        and also above 20!



# Example 1.13 : If statements cannot be empty , but for some reason we have empty content put "pass" keyword to avoid error
a = 33
b = 200

if b > a:
  pass      # having an empty if statement like this, would raise an error without the pass statement
