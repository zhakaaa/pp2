#REMOVE LIST ITEMS


# Example 5.1 : 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # apple cherry


# Example 5.2 : If there are more specified values , the function "remove" will remove the first one
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  #apple cherry banana kiwi


# Example 5.3 : Remove ar specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #apple cherry


# Example 5.4 : If you don't specify the index , function "pop" will remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #apple banana


# Example 5.5 : The function "del" also removes items at specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # banana cherry


# Example 5.6 : If you don't specify the index, function "del" will delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #And it cause error , because function delete list with content.


# Example 5.7 : The function "clear" delete list completely.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # there will be empty list [], because function delete content not list.

