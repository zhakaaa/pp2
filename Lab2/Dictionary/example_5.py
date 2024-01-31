# REMOVING ITEMS FROM DICTIONARY


# Example 5.1 : Delete item with "pop()" using specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)    # {'brand': 'Ford', 'year': 1964}


# Example 5.2 : The method "popitem()" delete last item or random item 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)        # {'brand': 'Ford', 'model': 'Mustang'}



# Example 5.3 : The "del" keyword removes with specified key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)     # {'brand': 'Ford', 'year': 1964}



# Example 5.4 : The "del" keyword can remove dict completely
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)  # error



# Example 5.5 : The method "clear()" remove content of dict , but not dict itself
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)   # {e}


  


