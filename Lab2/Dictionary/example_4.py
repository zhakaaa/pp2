# ADD ITEMS TO DICTIONARY


# Example 4.1 : Adding item to dict is done by using new key and value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}



# Example 4.2 : Adding item to dict is done by using method "update()"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})   
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}