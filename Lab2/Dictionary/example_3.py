#CHANGE ITEMS IN DICT


# Example 3.1 : Change the year to 2018
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# Example 3.2 : Change item with method "update()". argument must be dictionary or value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})   # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}





