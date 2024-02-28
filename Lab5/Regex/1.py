import re

txt = "sdfsfasabb ssf ab asdb"
y = txt.split(" ")

for i in y :
    x = re.findall(".*a.*|.*ab.*",i)
    if x :
        print(x)
    