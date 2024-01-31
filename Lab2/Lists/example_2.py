#ACCESS TO LIST'S ITEMS

# Example 2.1 : 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # banana


# Example 2.2 : 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry


# Example 2.3 : The first index is included , but the second index is not included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # cherry, orange, kiwi


# Example 2.4 : Return items from the begining until 4 index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# Example 2.5 : Return items from 2 index until the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# Example 2.6 : Return items from -4 index until -1 index.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Example 2.7 : Check item
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #true