# ACCESS TO DICT ITEMS

# Example 2.1 : 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)   # Mustang



# Example 2.2 : We can access to item with method "get()"
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)



# Example 2.3 : The method "keys()" return list of all keys in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)   # dict_keys(['brand', 'model', 'year'])



# Example 2.4 : The method "values()" return list of all values in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x)   # dict_values(['Ford', 'Mustang', 1964])



# Example 2.5 : We add new key : value pair
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()                               
print(x) #before the change   dict_keys(['brand', 'model', 'year'])

car["color"] = "white"
print(x) #after the change    dict_keys(['brand', 'model', 'year', 'color'])



# Example 2.6 : We change the value of "year" key and add new key : value pair 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change    dict_values(['Ford', 'Mustang', 2020])

car["year"] = 2020
print(x) #after the change     dict_values(['Ford', 'Mustang', 2020])

car["color"] = "red"
print(x) #after the change     dict_values(['Ford', 'Mustang', 2020, red'])



# Example 2.7 : The method "items()" returns all items in dict, as tuple in list
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)     # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Example 2.8 : We changed items in dict and can see the difference
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change    dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020
print(x) #after the change     dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car["color"] = "red"
print(x) #after the change    dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'red')])


# Example 2.9 : Check if the key in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") # Yes, 'model' is one of the keys in the thisdict dictionary



