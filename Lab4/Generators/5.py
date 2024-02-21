n = int(input())

def gen(n) :
    for i in range(n,0,-1) :
        yield i
    
for j in gen(n) :
    print(j)