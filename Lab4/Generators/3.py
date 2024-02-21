n = int(input())

def gen_func(n) :
    
    for i in range(n) :
        if i % 3 == 0 and i % 4 == 0 :
            yield i
            
for i in gen_func(n) :
    print(i)