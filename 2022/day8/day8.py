import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
m = parse_matrix()

def vertical_down(m,y,x):
    n = []
    for i in range(y+1,len(m)):
        n.append(m[i][x])
    return n

def horizontal_right(m,y,x):
    n = []
    for i in range(x+1,len(m)):
        n.append(m[y][i])
    return n

def horizontal_left(m,y,x):
    n = []
    for i in range(x-1,-1,-1):
        n.append(m[y][i])
    return n

def vertical_up(m,y,x):
    n = []
    for i in range(y-1,-1,-1):
        n.append(m[i][x])
    return n


def view(m,y,x,n):
    l = []
    for item in n:
        if item > m[y][x]:
            l.append(item)
            break
        if item < m[y][x]:
            l.append(item)
        if item == m[y][x]:
            l.append(item)
            break
    return len(l)

visible = 0
score = 0

for y in range(len(m)):
    for x in range(len(m[0])):
        vu = vertical_up(m,y,x)
        hr = horizontal_right(m,y,x)
        hl = horizontal_left(m,y,x)
        vd = vertical_down(m,y,x)
        ls = [vu,hr,hl,vd]
        
        score = max(score,math.prod(l_map(lambda l: view(m,y,x,l),ls)))
        
        if x == len(m[0])-1 or x == 0 or y == len(m)-1 or y == 0:
            visible += 1
        elif any(l_map(lambda l: all([item < m[y][x] for item in l]),ls)):
            visible += 1
        
print(visible)
print(score)


