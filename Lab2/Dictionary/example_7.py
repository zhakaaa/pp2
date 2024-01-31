#COPYING DICTIONARIES


# Example 7.1 : Copy dict by using method "copy()"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)       # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Example 7.2 : Copy dict by using "dict" keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)       # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}e
