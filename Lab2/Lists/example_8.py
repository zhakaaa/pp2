#SORT LIST


# Example 8.1 : The method "sort" will sort the list alphanumerically, ascending order.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']


# Example 8.2 : Sort the numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  #[23, 50, 65, 82, 100]


# Example 8.3 : Sort in descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)  #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]


# Example 8.4 : We can sort the list by our own function , rule.
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)  #[50, 65, 23, 82, 100]


# Example 8.5 :All capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)   #['Kiwi', 'Orange', 'banana', 'cherry']


# Example 8.6 : So if you want a case-insensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']


# Example 8.7 : The method "reverse" will reverse the list 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)   #['cherry', 'Kiwi', 'Orange', 'banana']