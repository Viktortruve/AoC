import sys
sys.path.append("..")
from AoC_parser import *
from functools import cmp_to_key


ls = []
pair = 0
c = 0
def recur(l1,l2):
    if type(l1) == int and type(l2) == int:
        if l1 > l2:
            return -1
        elif l1 < l2:
            return 1
        else:
            return 0 
    
    if type(l1) == int and type(l2) == list:
        return recur([l1],l2)
    
    if type(l1) == list and type(l2) == int:
        return recur(l1,[l2])
    
    if type(l1) == list and type(l2) == list:
        if l1 and not l2:
            return -1     
        if not l1 and l2:
            return 1
        if not l1 and not l2:
            return 0
        else:
            x = recur(l1[0],l2[0])
            return x if x != 0 else recur(l1[1:],l2[1:])
        
    
sorted_lols = [[2],[6]]
with open("input.txt") as file:
    for line in file:
        if len(line) > 1:
            l = eval(line.strip())
            ls.append(l)
            sorted_lols.append(l)
            if len(ls) == 2:
                order = []
                pair += 1                    
                val = recur(ls[0],ls[1])
                if val == 1:
                    c += pair
                ls = []
sorted_lols.sort(key=cmp_to_key(recur),reverse=True)
print(c)
print((sorted_lols.index([2])+1)*(sorted_lols.index([6])+1))


            
        