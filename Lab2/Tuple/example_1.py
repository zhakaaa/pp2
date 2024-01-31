#TUPLE

thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
Tuples are ordered , changeable , indexed and allow duplicates.
Ordered means items of tuple have defined order and this order will not change. The new item will be added at the end of tuple.
Unchangeable means items cannot be removed, added or changed.
Indexed means we can access to specific items in the tuple through index.
Allow duplicates means tuples can store same items.
'''

# Example 1.1 : Print number of items in tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  #3

thistuple = ("apple",)
print(type(thistuple))  # this is tuple


# Example 1.2 : NOT a tuple
thistuple = ("apple")   
print(type(thistuple))  # this is string


# Example 1.3 : Tuple can contain different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # <class 'tuple'>


# Example 1.4 : Create etuple with method "tuple"
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)