lst = []
size = int(input())

for i in range(size) :
    x = input()
    lst.append(x)


f = open("4.txt" , "a")

for i in lst :
    f.write("\n" + i)
    
f.close()

f = open("4.txt" , "r")
print(f.read())