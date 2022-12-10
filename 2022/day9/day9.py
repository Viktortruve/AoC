import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
def move_tail(head,tail):

    x1,y1 = tail 
    x2,y2 = head
    
    if x1 == x2 and y1 < y2 :
        return (x1,y1+1)
    
    elif x1 == x2 and y1 > y2:
        return(x1,y1-1)
    
    elif x1 > x2 and y1 == y2:
        return (x1-1,y1)
    
    elif x1 < x2 and y1 == y2:
        return(x1+1,y1)
    
    elif x1 > x2 and y1 > y2:
        return(x1-1,y1-1)

    elif x1 > x2 and y1 < y2:
        return(x1-1,y1+1)

    elif x1 < x2 and y1 < y2:
        return (x1+1,y1+1)
    
    elif x1 < x2 and y1 > y2:
        return (x1+1,y1-1)


def trailing(head,tail):
    return abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1

def solve(knots):
    visited = defaultdict(int)
    visited[(0,0)] += 1
    with open("input.txt") as file:
        for line in file:
            s = line.strip().split(" ")
            dir = s[0]
            length = int(s[1])
            
            for _ in range(length):
                tmp_head = knots[0]

                if dir == "L":
                    knots[0] =(tmp_head[0]-1,tmp_head[1])
                
                if dir == "R":
                    knots[0] =(tmp_head[0]+1,tmp_head[1])
            
                if dir == "U":
                    knots[0] =(tmp_head[0],tmp_head[1]+1)
                
                if dir == "D":
                    knots[0] =(tmp_head[0],tmp_head[1]-1)
                
                for k in range(len(knots)-1):
                    tail = knots[k+1]
                    head = knots[k]
                    if trailing(head,tail):
                        tail = move_tail(head,tail)
                        knots[k+1] = tail
                
                visited[knots[len(knots)-1]] += 1
            
    return len(visited)

knots = [(0,0) for _ in range(10)]
print(solve(knots[0:2]))
print(solve(knots))
    
            



