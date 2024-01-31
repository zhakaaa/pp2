x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #true
print(x is y) #false
print(x == y) #true


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) #false
print(x is not y) #true
print(x != y)     #false
