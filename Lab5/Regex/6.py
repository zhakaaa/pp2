import re

txt = input()

x = re.sub("\s", ":",txt)

if x:
    y = re.sub("\." , ":" , x)
    if y :
        z = re.sub("\," , ":" , y)
        print(z)
    else :
        print(y)
else :
    print(x)
        
    

