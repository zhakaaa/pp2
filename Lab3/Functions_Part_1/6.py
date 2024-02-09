#reverse string

word = input("Enter: ")

lst = []

txt = word.split()

for i in txt :
    lst.append(i)
    
lst.reverse()

print(lst)