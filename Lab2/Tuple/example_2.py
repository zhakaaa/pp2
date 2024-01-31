#ACCESS TO TUPLE ITEMS


# Example 2.1 : 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # print the second value in tuple


# Example 2.2 : 
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # print the lasr value in tuple


# Example 2.3 : 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Return the third, fourth, and fifth value


# Example 2.4 : 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])   # returns the items from the beginning to specified index, but NOT included, "kiwi"


# Example 2.5 : 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])  # returns the items from "cherry" and to the end


# Example 2.6 : 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  #  returns the items from index -4 (included) to index -1 (excluded)


# Example 2.7 : 
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")   #Yes, 'apple' is in the fruits tuple

