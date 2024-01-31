# LOOP DICTIONARIES


# Example 6.1 : Print all key names in dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)   # brand /n model /n year



# Example 6.2 : Print all values in dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])   # Ford /n Mustang /n 1964


# Example 6.3 : Print all values by using "values()" method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)      # Ford /n Mustang /n 1964



# Example 6.4 : Print all keys by using "keys()" method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)       # brand /n model /n year



# Example 6.5 : Print all items in dict by using "items()" method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)        # brand Ford /n model Mustang /n year 1964e



