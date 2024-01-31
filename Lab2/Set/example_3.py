#ADD ITEMS TO SET


# Example 3.1 : We cannot change items of set , but we can add new valus to it
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# Example 3.2 : To copy values of another set use method "update"
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)    # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


# Example 3.3 : The object in method "update" can be any iterable object : tuples , lists , set and etc
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)    # e{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
