#JOIN TUPLES


# Example 6.1 : Concatenate tuples by "+" operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)    # ('a', 'b', 'c', 1, 2, 3)


# Example 6.2 : If we want to multiply the content of a tuple a given number of times , we use "*" operator
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
   
print(mytuple)   # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
