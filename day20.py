import numpy as np
import networkx as nx
from collections import defaultdict, Counter
import itertools

def manhattan(p,q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def matrix_to_graph(matrix, neighbor_func):
    G = nx.Graph()
    for i in range(len(matrix)):
         for j in range(len(matrix[0])):
                G.add_node((i,j))
    for node in G.nodes:
        row,col = node
        neighs = neighbor_func(matrix,row,col)
        for neigh in neighs:
            G.add_edge(node,neigh)
    return G
def parse_matrix():
    l = []
    with open("day20.txt") as file:
        for line in file:
            x = []
            for ele in line:
                x.append(ele.strip())
            
            l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
    return np.array(l, dtype=object)

def outside_matrix(curr, m):
    return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

def neighbors(matrix, row,col):
    if m[row][col] == "#":
        return []
    n1 = (row+1, col)
    n2 = (row-1, col)
    n3 = (row, col+1)
    n4 = (row, col-1)
    ns = [n1, n2, n3, n4]
    ns = [item for item in ns if not outside_matrix(item, matrix)]
    ns = [item for item in ns if matrix[item] != "#"]
    return ns

m = parse_matrix()
start = tuple(np.argwhere(m=="S")[0])
end = tuple(np.argwhere(m=="E")[0])
G = matrix_to_graph(m, neighbors)
shortest_path = nx.astar.astar_path(G, start, end)
shortest_path_len = len(shortest_path)    
costs = defaultdict(int)
for i, node in enumerate(shortest_path):
    costs[node] = shortest_path_len - i
distances = []
for u,v in itertools.combinations(shortest_path, 2):
    md = manhattan(u,v)
    if md > 20:
        continue
    dist = costs[u] - costs[v] - md
    if dist >= 100:
        distances.append(dist)
s = Counter(distances)
print(sum(list(s.values())))

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

