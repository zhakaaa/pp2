#UNPACK TUPLE


# Example 4.1 : When we create tuple and assign values to it is called - packing tuple
fruits = ("apple", "banana", "cherry")
print(fruits)


# Example 4.2 : When we extract values back into variables it is called - unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


# Example 4.3 : If the number of variables less than number of values in tuple , then we use '*' to extract remaining values. assign rest of the values as list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)    # apple
print(yellow)   # banana
print(red)      # ['cherry', 'strawberry', 'raspberry']


# Example 4.4 : If artisk assign to another variable than the last , then python will assign values to variable until number of left values matches number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)   # apple
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red)     # cherry