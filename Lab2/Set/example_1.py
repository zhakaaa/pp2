#SET

myset = {"apple", "banana", "cherry"}
print(myset)


'''
Sets are unordered , unchangeable , unindexed and not allow duplicates.
Unordered means items of set have undefined order . so , items will appear in random order
Unchangeable means items cannot be changed , but you can remover or add values.
Unindexed means we cannot access to specific items in the set through index.
Not allow duplicates means sets cannot store same items.
'''


# Example 1.1 : Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)   # {'banana', 'cherry', 'apple'}


# Example 1.2 : The values True and 1 considered as same value, so one of them will not appear
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)    # {True, 2, 'banana', 'cherry', 'apple'}


# Example 1.3 : The values False and 0 considered as same value, so one of them will not appear
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)    # {False, True, 'cherry', 'apple', 'banana'}


# Example 1.4 : The length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # 3


# Example 1.5 : Sets can contain different data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


# Example 1.6 : Data type of set is - set
myset = {"apple", "banana", "cherry"}
print(type(myset))   # <class 'set'>


# Example 1.7 : We can use constructor "set" to make set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)   # {'cherry', 'banana', 'apple'}
