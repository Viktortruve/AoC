import numpy as np
def parse_matrix():
	l = []
	with open("day12.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l, dtype=object)

def outside_matrix(curr, m):
	return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

directions = [
	[0,1],
	[0,-1],
	[1,0],
	[-1,0]
]
def map_region(m, cord, l):
	ns = map(lambda x: (cord[0]+x[0], cord[1]+x[1]),directions)
	ns = filter(lambda x: not outside_matrix(x,m) and x not in l, ns)
	ns = list(filter(lambda x: m[x] == m[cord], ns))
	if not ns:
			return l
	else:
		for n in ns:
			l.add(n)
			l.update(map_region(m, n, l))
	return l
def distance(n1,n2):
	x1,y1 = n1
	x2,y2 = n2
	return abs(x2-x1) + abs(y2-y1)


def perimeter(region, m):
	perimeter = 0
	for cord in region:
		neighbors = list(map(lambda x: (cord[0]+x[0], cord[1]+x[1]),directions))
		neighbors_on_border = [item for item in neighbors if item[0] == -1 or item[0] == len(m) or item[1] == -1 or item[1] == len(m)]
		neighbors_inside_matrix = list(filter(lambda x: not outside_matrix(x,m), neighbors))
		neighbors_inside_matrix = list(filter(lambda x: m[x] != m[cord], neighbors_inside_matrix))
		perimeter_points = set(neighbors_inside_matrix + neighbors_on_border)
		perimeter += len(perimeter_points)
	return perimeter	

def price_p1(region, m):
	r_perimeter = perimeter(region, m)
	price = r_perimeter*len(region)
	return price

def sides(region, m):
	return 1

def price_p2(region, m):
	r_sides = sides(region, m)
	price = r_sides*len(region)
	return price

m = parse_matrix()
regions = set()
for col in range(len(m)):
		for row in range(len(m)):
				s = set()
				s.add((col, row))
				region = map_region(m, (col,row), s)
				regions.add(frozenset(region))
print(sum(map(lambda x: price_p1(x, m), regions)))
print(sum(map(lambda x: price_p2(x, m), regions)))

# too high 1393840