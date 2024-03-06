f = open("4.txt" , "r")
g = open("7.txt" , "w")

for i in f :
    g.write(i)

f.close()
g.close()

g = open("7.txt" , "r")
print(g.read())