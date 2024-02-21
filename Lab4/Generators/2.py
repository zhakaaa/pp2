n = int(input())
lst = []

gen_func = (i for i in range(n) if i % 2 == 0)

for i in gen_func :
    lst.append(i)
    
print(lst)
