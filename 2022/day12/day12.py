import sys
sys.path.append("..")
from AoC_parser import *
from pprint import pprint
from collections import defaultdict
import math
import os
from queue import PriorityQueue

m = parse_matrix()



org_start = np.argwhere(m=="S")[0]
goal = np.argwhere(m=="E")
m[goal[0][0]][goal[0][1]] = 'z'
m[org_start[0]][org_start[1]] = 'a'


starts = np.argwhere(m == 'a')
path_s = 100000
for start in starts:
    visited = set()
    queue = []
    pq = PriorityQueue()
    values = defaultdict(lambda: 10000)
    current = (start[0],start[1])
    pq.put((0,(current[0],current[1])))
    values[(current[0],current[1])] = 0
    
    while not pq.empty():
        dist,current = pq.get()
        visited.add(current)
        neighbors = matrix_all_neighbors(m,current[0],current[1],flag=True)[0][:4] 
        for neighbor in neighbors:
            f = [item for item in neighbors if item[0] < len(m) and item[0] >= 0 and item[1] < len(m[0]) and item[1] >= 0]
            for n in f:
                row,col = n[0],n[1]
                elevation = ord(m[row][col]) - ord(m[current[0]][current[1]]) 
                
                if elevation <= 1 and (row,col) not in visited:
                    old_cost = values[(row,col)]
                    new_cost = values[(current[0],current[1])] + 1
                    if new_cost < old_cost:
                        values[(row,col)] = new_cost
                        pq.put((new_cost,(row,col)))
    if np.array_equal(start,org_start):
        print(values[(goal[0][0],goal[0][1])])
    path_s = min(values[(goal[0][0],goal[0][1])],path_s)
print(path_s)
             

