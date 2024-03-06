def gen_files(letter) :
    f = open(letter, "x")
    

letter = 'A'
for i in range(26) :
    gen_files(letter)
    letter = chr(ord(letter) + 1)


    
    