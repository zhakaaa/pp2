import re

txt = input() 

x = re.sub(r"_([a-zA-Z])" ,lambda x:  x.group(1).upper() ,txt)

print(x)
