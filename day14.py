from dataclasses import dataclass
robots = []

with open("day14.txt") as file:
    for line in file:
        if not line:
            continue
        l = line.strip().split("v=")
        p = l[0].split("=")[1]
        v = l[1]
        print(p,v)
        p = [int(item) for item in p.split(",")]
        v = [int(item) for item in v.split(",")]
        robots.append((p,v))

def move(robot):
    new_x = robot[0][0] + robot[1][0]
    new_y = robot[0][1] + robot[1][1]
    if new_x >= x_lim:
        new_x = new_x-x_lim
    if new_y >= y_lim:
        new_y = new_y-y_lim 
    if new_x < 0:
        new_x = x_lim-abs(new_x)
    if new_y < 0:
        new_y = y_lim-abs(new_y)       
    robot[0][0] = new_x
    robot[0][1] = new_y
    return robot

def safety_count(robots):
    safe_robots = [robot for robot in robots if robot[0][0] != x_lim//2 and robot[0][1] != y_lim//2]
    quadrants = defaultdict(int)
    quad_count = defaultdict(int)
    for y in range(0, y_lim//2):
        for x in range(0,x_lim//2):
            quadrants[x,y] = 1
        for x in range(x_lim//2, x_lim):
            quadrants[x,y] = 2 
    
    for y in range(y_lim//2, y_lim):
        for x in range(0,x_lim//2):
            quadrants[x,y] = 3
        for x in range(x_lim//2, x_lim):
            quadrants[x,y] = 4
    for robot in safe_robots:
        pos = robot[0]
        quadrant = quadrants[(pos[0],pos[1])]
        quad_count[quadrant] += 1
    return quad_count


x_lim = 101
y_lim = 103

directions = [
    [0,1],
    [1,0],		
    [0,-1],
    [-1,0],
    [-1,1],
    [1,1],
    [1,-1],
    [-1,-1],    
]
def map_region(pos, l):
    ns = map(lambda x: (pos[0]+x[0], pos[1]+x[1]),directions)
    ns = list(filter(lambda x: [x[0], x[1]] in [item[0] for item in robots] and x not in l, ns))
    if not ns:
        return l
    else:
        for n in ns:
            l.add(n)
            l.update(map_region([n[0],n[1]], l))
    return l

from collections import defaultdict
import math
max_size = 0
for i in range(10000):
    robots = list(map(move, robots))
    positions = [item[0] for item in robots]
    l = list(map(lambda x: map_region(x, {tuple(x)}), positions))
    max_region = max([len(item) for item in l])
    if max_region > max_size:
        max_size = max_region
        print(i+1, max_region)
#safe_robots = [robot for robot in robots if robot[0][0] != x_lim//2 and robot[0][1] != y_lim//2]
#positions = sorted([item[0] for item in safe_robots], key = lambda x: (x[1],x[0]))
quad_count = safety_count(robots)

print(math.prod(quad_count.values()))
from pprint import pprint


# 7708 too low