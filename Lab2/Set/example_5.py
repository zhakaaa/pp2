#JOIN SETS


# Example 5.1 : With method "union()"  we can concatenate sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)    # {3, 2, 1, 'a', 'b', 'c'}


# Example 5.2 : We can add another set  with method "update()"
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)   #  {'c', 1, 3, 'a', 2, 'b'}


# Example 5.3 : The method "intersection_update()" keeps values that present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)    # {'apple'}


# Example 5.4 : The method "intersection()" return new set of values that present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)  # {'apple'}


# Example 5.5 : The method "symmetric_difference_update" keeps values that NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)    # {'google', 'banana', 'microsoft', 'cherry'}


# Example 5.6 : The method "symmetric_difference()" return new set of values that  NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)


# Example 5.7 : The values True and 1 considered as same values and the method will not print them
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)   # {2, 'google', 'cherry', 'banana'}
