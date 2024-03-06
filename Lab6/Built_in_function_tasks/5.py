from functools import reduce
import operator

tpl = (True,True,True,True)

if reduce(operator.eq,tpl) :
    print(True)
else :
    print(False)