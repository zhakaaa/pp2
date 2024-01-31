#UPDATE TUPLES


# Example 3.1 : We cannot change the values of tuple , but we can convert tuple to list and change the value of list and convert back to tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)   #("apple", "kiwi", "cherry")


# Example 3.2 : Add new value to tuple by method "append" and "list"
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)  # ('apple', 'banana', 'cherry', 'orange')


# Example 3.3 : Add new value to tuple by concatenation
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)   # ('apple', 'banana', 'cherry', 'orange')


# Example 3.4 : Remove values from tuple by method "remove" and "list"
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)   # ('banana', 'cherry')


# Example 3.5 : Delete values of tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
