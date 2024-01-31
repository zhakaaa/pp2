#LISTS
thislist = ["apple", "banana", "cherry"] 
print(thislist)
'''
Lists are ordered , changeable , indexed and allow duplicates.
Ordered means items of list have defined order and this order will not change. The new item will be added at the end of list.
Changeable means items can be removed, added , changed.
Indexed means we can access to specific items in the list through index.
Allow duplicates means lists can store same items.
'''

# Example 1.1 : List allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# Example 1.2 : Length of list is 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# Example 1.3 : Lists items can be any of data types
list1 = ["apple", "banana", "cherry"] #string
list2 = [1, 5, 7, 9, 3]               #int
list3 = [True, False, False]          #boolean


# Example 1.4 : Also can store different data types
list1 = ["abc", 34, True, 40, "male"]


# Example 1.5 : Data type of list is - 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# Example 1.6 : We can use constructor 'list' to create list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)