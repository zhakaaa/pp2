# Unique Numbers

lst = []
size = int(input("Enter the size of list: "))

for x in range(0,size) :
    number = int(input())
    lst.append(number)
    
def unique_numbers(lst) :
    for x in range(0,size) :
        a = True
        for y in range(0,size) :
            if x != y: 
                if lst[x] == lst[y] :
                    a = False
                    break
                
        if a :
            print(lst[x])

print("unique numbers : ")
unique_numbers(lst)
             