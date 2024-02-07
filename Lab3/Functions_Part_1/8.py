#Write a function that takes in a list of integers and returns True if it contains 007 in order

lst = []
size = int(input("enter size: "))

for i in range(size) :
    number = int(input())
    lst.append(number)
    
def spy_game(lst) :
    a = False
    for i in range(size) :
        if lst[i] == 0 and lst[i+1] == 0 and lst[i+2] == 7 :
            a = True
            break
        
    print(a)
        
spy_game(lst)