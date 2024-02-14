# We can convert Python objects of the following types, into JSON strings:

import json

print(json.dumps({"name": "John", "age": 30})) # {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))        # ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))        # ["apple", "bananas"]
print(json.dumps("hello"))                     # "hello"
print(json.dumps(42))                          # 42      
print(json.dumps(31.76))                       # 31.76
print(json.dumps(True))                        # true
print(json.dumps(False))                       # false
print(json.dumps(None))                        # null
