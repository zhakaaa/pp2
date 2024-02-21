a = int(input())
b = int(input())

def squares() :
    for i in range(a, b) :
        yield i ** 2
        
for i in squares() :
    print(i)