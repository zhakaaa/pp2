# DICTIONARY

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)    # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


'''
Dictionaries are ordered , changeable and not allowed duplicates.
Ordered means items of dictionary have defined order.
Changeable means items can be removed, added , changed.
Not allowed duplicates means dictionary cannot store same items.
'''

# Example 1.1 : Dictionary cannot have two values with same keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)   #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Example 1.2 : Print the length of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))  # 3


# Example 1.3 : The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)   # {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}


# Example 1.4 : Data type of dictionary is - 'dict'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))    # <class 'dict'>


# Example 1.5 : We can use constructor "dict()" to create dict
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
