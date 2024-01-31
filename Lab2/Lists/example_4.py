#ADD LIST ITEMS

# Example 4.1 : 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # apple banana cherry orange

# Example 4.2 : Function "insert" will add new value to specific place and length of list will increase
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # apple orange banana cherry
print(thislist)

# Example 4.3 : With function "extend" we can add another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # apple banana cherry mango pineapple papaya

# Example 4.4 : With function "extend" you can add any iterable data types : tuple,set,dict and etc.e
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)