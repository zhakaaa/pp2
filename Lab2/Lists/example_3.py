#CHANGE ITEM VALUE

# Example 3.1 : 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"  # change the second value
print(thislist)

# Example 3.2 : Change the range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 3.3 : The new item will be inserted where you specified
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)