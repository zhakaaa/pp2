# Filter prime in list of numbers


lst = []
size = int(input("enter size: "))

for i in range(size):
    number = int(input())
    lst.append(number)
    
def prime_numbers(lst) :
    for i in lst :
        a = True
        if i == 1 or i == 0:
            continue
        else :
            for x in range(2,i) :
                if i % x == 0 :
                    a = False
                    break
        
        if a :
            print(i)

print("prime numbers: ")        
prime_numbers(lst)        