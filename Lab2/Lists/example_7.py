#LIST COMPREHENSION


# Example 7.1 : 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)   #apple /n banana /n mango


# Example 7.2 : List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  #apple /n banana /n mango


# Example 7.3 : 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist) #banana /n cherry /n kiwi /n mango


# Example 7.4 : Without condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) # "apple" /n "banana" /n "cherry" /n "kiwi" /n "mango"


# Example 7.5 : Iterable can be any iterable object : tuple , list , set , dict and etc
newlist = [x for x in range(10)]
print(newlist) # 0 1 2 3 4 5 6 7 8 9 

newlist = [x for x in range(10) if x < 5]
print(newlist) # 0 1 2 3 4 


# Example 7.6 : You can manipulate with expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# Example 7.7 : 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) #['hello', 'hello', 'hello', 'hello', 'hello']


# Example 7.8 : Expression can also have condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


