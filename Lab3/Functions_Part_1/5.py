#permutation

from itertools import permutations 
 
txt = input("Enter some txt: ")

perm = permutations(txt) 
 
for i in list(perm): 
    print (i) 