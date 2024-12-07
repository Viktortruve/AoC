import numpy as np
def parse_matrix():
	l = []
	with open("day6.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l)

m = parse_matrix()
def outside_matrix(curr):
    return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

start = np.argwhere(m == "^")[0]
dirs = [[-1,0], [0,1], [1,0], [0,-1]]
dir = 0
from collections import defaultdict
distinct_visited = defaultdict(int)
distinct_visited[tuple(start),0] += 1
curr = start 
m[start[0]][start[1]] = "."
while True:
    direction = dirs[dir]
    next_coord = (curr[0]+direction[0],curr[1]+direction[1])
    if outside_matrix(next_coord):
        break
    next_val = m[next_coord[0]][next_coord[1]]
    if next_val != ".":
        dir += 1 
        if dir == len(dirs):
            dir = 0
        continue
    else:
        curr = next_coord
        distinct_visited[curr, dir] += 1

traversed_points = list([item[0] for item in distinct_visited.keys()])
possibilites = 0
traversed_points = [item for item in traversed_points if item != (start[0],start[1])]
traversed_points = list(set(traversed_points))
for i, p in enumerate(traversed_points):
    dir = 0
    distinct_visited = defaultdict(int)
    distinct_visited[tuple(start), dir] += 1
    curr = start
    while True:
        direction = dirs[dir]
        next_coord = (curr[0]+direction[0],curr[1]+direction[1])
        if (next_coord, dir) in distinct_visited:
             possibilites += 1
             break
        if outside_matrix(next_coord):
            #print("GOT OUT", p)
            break
        next_val = m[next_coord[0]][next_coord[1]]
        if next_val != "." or next_coord == p:
            dir += 1 
            if dir == len(dirs):
                dir = 0
            continue
        else:
            curr = next_coord
            distinct_visited[curr, dir] += 1
print(possibilites)