#LOOP THROUGH THE LIST


# Example 6.1 : 
thislist = ["apple", "banana", "cherry"]    # apple \n banana \n cherry
for x in thislist:
  print(x)


# Example 6.2 : Also we can loop through the list by referring to their index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Example 6.3 : Also we can loop the list through while loop by referring to their index
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Example 6.4 : Loop the list by list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]        # apple \n banana \n cherry
#do this / in this collection / in this situation