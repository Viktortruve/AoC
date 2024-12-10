
import networkx as nx
import numpy as np

def matrix_to_graph(matrix, neighbor_func):
	G = nx.DiGraph()
	node_count = 0
	for i in range(len(matrix)):
		 for j in range(len(matrix[0])):
				G.add_node(node_count, pos=(i,j))
				node_count += 1
	pos=nx.get_node_attributes(G,'pos')
	rev_pos = {v:k for k,v in pos.items()}
	for node in G.nodes:
		row,col = pos[node]
		neighs = neighbor_func(matrix,row,col)
		for neigh in neighs:
				G.add_edge(node,rev_pos[neigh])	
	return G

def neighbors(matrix, row,col):
	if not isinstance(matrix[row][col], int):
		return [] 
	n1 = (row+1, col)
	n2 = (row-1, col)
	n3 = (row, col+1)
	n4 = (row, col-1)
	ns = [n1, n2, n3, n4]
	ns = [item for item in ns if not outside_matrix(item, matrix)]
	ns = [item for item in ns if matrix[item] == matrix[row][col]+1]
	return ns

def outside_matrix(curr, m):
	return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

def parse_matrix():
	l = []
	with open("day10.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l, dtype=object)

m = parse_matrix()
starts = np.argwhere(m==0)
goals = np.argwhere(m==9)
starts = [tuple(item) for item in starts]
goals = [tuple(item) for item in goals]
G = matrix_to_graph(m, neighbors)
pos=nx.get_node_attributes(G,'pos')
rev_pos = {v:k for k,v in pos.items()}
paths = []
path_count = 0
for start in starts:
		for goal in goals:
			try:
				paths.append(nx.astar.astar_path(G, rev_pos[start], rev_pos[goal]))
				path_count += len(list(nx.all_simple_paths(G, rev_pos[start], rev_pos[goal])))		
			except:
				pass
print(len(paths))
print(path_count)