import numpy as np

lst = []

size = int(input())

for i in range(size) :
    value = int(input())
    lst.append(value)


result = np.prod(lst)

print(result)





