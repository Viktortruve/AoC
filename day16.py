
import networkx as nx
import numpy as np

def matrix_to_graph(matrix, neighbor_func):
    G = nx.DiGraph()
    for i in range(len(matrix)):
         for j in range(len(matrix[0])):
            for direction in directions:
                G.add_node((i, j, direction))
        
    edges = []
    for node in G.nodes:
        row,col,direction = node
        neighs = neighbor_func(matrix,row,col, direction)
        for neigh in neighs:
            edges.append(neigh)
    for edge in edges:
        u = (edge[0][0], edge[0][1], edge[2])
        v = (edge[1][0], edge[1][1], edge[3])
        weight = edge[4]
        G.add_edge(u, v,weight=weight)
    return G

def neighbors(matrix, row,col, direction):
    other_dirs = [item for item in directions if item != direction]
    n1 = ((row,col), (row+direction[0], col+direction[1]), direction, direction, 1)

    ns = []
    for d in other_dirs:
        if d == (direction[0]*-1, direction[1]*-1):
            continue
        else:
            ns.append( ((row,col),(row,col),direction, d, 1000))
    if not outside_matrix((row+direction[0], col+direction[1]), matrix):
        if matrix[row+direction[0]][col+direction[1]] != "#":
            ns.append(n1)
    return ns

def outside_matrix(curr, m):
    return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

def parse_matrix():
    l = []
    with open("day16.txt") as file:
        for line in file:
            x = []
            for ele in line:
                x.append(ele.strip())
            l.append([int(item) if item.isnumeric() else item for item in x if item != ''])
    return np.array(l, dtype=object)

m = parse_matrix()
directions = [
    (0,1),
    (-1,0),
    (0,-1),
    (1,0)
]

start_cord = tuple(np.argwhere(m=="S")[0])
goal_cord = tuple(np.argwhere(m=="E")[0])
start = (start_cord[0],start_cord[1],(0,1))
G = matrix_to_graph(m, neighbors)
goals = [item for item in G.nodes if item[0] == goal_cord[0] and item[1] == goal_cord[1]]
pws = []
paths = []
p1 = []
for goal in goals:
    shortest_paths = list(nx.all_shortest_paths(G, start, goal, weight="weight"))
    for path in shortest_paths: 
        paths.append([(item[0],item[1]) for item in path])
        path_weight = nx.path_weight(G, path, "weight")
        pws.append(path_weight)

shortest = [paths[i] for i in range(len(paths)) if pws[i] == min(pws)]
flat_list = [
    x
    for xs in shortest
    for x in xs
]
print(min(pws))
print(len(set(flat_list)))
