import numpy as np
import itertools
def parse_matrix():
	l = []
	with open("day8.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l)

def outside_matrix(curr):
	return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

def print_matrix(m):    
	print("".join(["".join(item)+'\n' for item in m]))

m = parse_matrix()
s = open("day8.txt").read()
chars = set(s)
chars = [item for item in chars if item not in [".",'\n']]

antinodes = set()
for char in chars:
	char_places = np.argwhere(m==char)
	pairs = itertools.combinations(char_places, 2)
	for pair in pairs:
		x1,y1 = pair[0]
		x2,y2 = pair[1]
		x_dist = x2 - x1
		y_dist = y2 - y1
		for j in range(len(m)):
			antinode_coord1 = x1 - x_dist*j, y1 - y_dist*j
			antinode_coord2 = x2 + x_dist*j, y2 + y_dist*j
			if not outside_matrix(antinode_coord1):
				antinodes.add(antinode_coord1)
			if not outside_matrix(antinode_coord2):
				antinodes.add(antinode_coord2)

print(len(antinodes))
print_matrix(m)