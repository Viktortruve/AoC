import numpy as np
import itertools
from pprint import pprint
import string
### Simple parse-matrix function 
def parse_matrix():
	l = []
	with open("input.txt") as file:
		for line in file:
			x = []
			for ele in line:
				x.append(ele.strip())
			l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
	return np.array(l)


### Flag used if index is what to be returned 
def matrix_all_neighbors(m,col,row,flag=None):
	n1 = matrix_vertical_neighbors(m,col,row,flag) if flag else matrix_vertical_neighbors(m,col,row)
	n2 = matrix_horizontal_neighbors(m,col,row,flag) if flag else matrix_horizontal_neighbors(m,col,row) 
	n3 = [(col-1,row-1),(col+1,row+1),(col-1,row+1),(col+1,row-1)] if flag else m[col-1][row-1],m[col+1][row+1],m[col-1][row+1],m[col+1][row-1]
	return np.array([n1,n2,n3])

def matrix_vertical_neighbors(m,col,row,flag=None):
	return np.array([(col+1,row), (col-1,row)] if flag else [m[col+1][row],m[col-1][row]])

def matrix_horizontal_neighbors(m,col,row,flag=None):
	return np.array([ (col,row+1), (col,row-1)] if flag else [ m[col][row+1], m[col][row-1] ])


## parse content of entire file based on separator
## Useful Example  --> Day 1 2022

def try_int(x): 
	s = x.strip()
	return int(s) if s.isnumeric() else s
def parse_file_by_separator(separator=" "):
	return l_map(try_int,open("input.txt").read().split(separator))

## Parse content line by line based on separator
def parse_line_by_separator(separator = " "):
	l = []
	with open("input.txt") as file:
		for line in file:
			s = line.strip().split(separator)
			ls = l_map(try_int,s)
			l.append(ls)
	return l

def all_combinatons(list,size):
	return list(itertools.combinations(list,size))

## Sugar to avoid list(map()) 
def l_map(expr,l):
	return list(map(expr,l))
## Sugar to avoid filter(map())
def l_filter(expr,l):
	return list(filter(expr,l))

def l_zip(l1,l2):
	return list(zip(l1,l2))


def read_file_in_chunks(chunk_size: int,split=False): 
	f = open("input.txt").readlines()
	if split:
		f = [item for item in f if item != '\n']
	return [ l_map(try_int,f[i:i+chunk_size]) for i in range(0,len(f),chunk_size)]

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        minimum = 100000000
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < minimum and sptSet[v] == False:
                minimum = dist[v]
                min_index = v
 		
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
'''
while not pq.empty():
dist, current = pq.get()
visited.add(current)

for neighbour in neighbours(lines, *current):
    distance = lines[neighbour]
    if neighbour not in visited:
        old_cost = values[neighbour]
        new_cost = values[current] + distance
        if new_cost < old_cost:
            pq.put((new_cost, neighbour))
            values[neighbour] = new_cost
'''

