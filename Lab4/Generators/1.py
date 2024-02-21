n = int(input())

def gen_func(n) :
    i = 0
    while i < n :
        yield i ** 2
        i+=1
    
for i in gen_func(n) :
    print(i)
    
