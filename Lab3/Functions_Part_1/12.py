# histogram

lst = []
size = int(input("enter size: "))

for i in range(size) :
    number = int(input())
    lst.append(number)
    
def histogram(lst) :
    b = ""
    for i in lst :
        a = ""
        for j in range(i) :
            a+="*"
        b+=a + " "
        #print(a)
    print(b)
        
histogram(lst)