lst = []
size = int(input("Enter size: "))

for i in range(size) :
    number = int(input())
    lst.append(number)
    
    
def filter_prime(number) :
    for i in range(2,number) :
        if number % i == 0:
            return False  
    return True
            
         
prime_number = lambda x : False if x == 1 or x == 0 else filter_prime(x)
prime_numbers = filter(prime_number, lst) 

print("Prime numbers : ")

for i in prime_numbers :
    print(i)














































































