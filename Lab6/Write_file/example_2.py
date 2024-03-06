f = open("demofile3.txt" , "w")   #  the "w" method will overwrite the entire file.
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt" , "r")
print(f.read())