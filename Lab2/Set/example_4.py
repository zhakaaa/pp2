# REMOVE ITEMS FROM SET


# Example 4.1 : To remove value from set we use method "remove()". if the item to remove doesn't exist , then it will cause ERROR
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)   # {'apple', 'cherry'}


# Example 4.2 : To remove value from set we use method "discard()". if the item to remove doesn't exist , then it will not cause ERROR
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)   # {'apple', 'cherry'}


# Example 4.3 : We can use method "pop()" to remove item from set, but it remove random item from set. Sets are unordered , so you cannot specify index to pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)    # return removed item
print(thisset)   # return set without removed item


# Example 4.4 : The method "clear()" delete all values of set , but not set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)    # set()


# Example 4.5 : The method "del" delete all values of set and set itself
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)   # cause an ERROR