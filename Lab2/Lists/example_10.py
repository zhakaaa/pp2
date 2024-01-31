#JOIN LIST


# Example 10.1 : Concatenate two lists 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)    #['a', 'b', 'c', 1, 2, 3]


# Example 10.2 : Another way to join two lists is by for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)    #['a', 'b', 'c', 1, 2, 3]


#Example 10.3 : Another way is by method "extend"
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)    #['a', 'b', 'c', 1, 2, 3]
