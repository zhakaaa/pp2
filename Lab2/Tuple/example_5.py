# LOOP


# Example 5.1 : We can loop through tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)     # apple /n banana /n cherry


# Example 5.2 : We can loop through tuple by indexes
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)) :
  print(thistuple[i])


# Example 5.3 : We can loop through tuple by while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple) :
  print(thistuple[i])
  i+=1   # i = i + 1