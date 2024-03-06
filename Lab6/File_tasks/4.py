f = open("4.txt" , "r")

count = 0
for i in f :
    count+=1

print(f"Number of lines in file {f} is {count}")