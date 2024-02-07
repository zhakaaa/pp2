#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

lst = []
size = int(input("enter size: "))

for i in range(size) :
    number = int(input())
    lst.append(number)
    
def has_33(lst) :
    a = False
    for i in range(0,size-1) :
        if lst[i] == 3 and lst[i+1] == 3 :
            a = True
            break
        
    print(a)
        
has_33(lst)