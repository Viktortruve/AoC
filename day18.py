blocks = [item.strip() for item  in open("day18.txt").readlines()]
blocks = [item.split(",") for item in blocks]
blocks = [(int(a), int(b)) for (a,b) in blocks]
import numpy as np
import networkx as nx

def matrix_to_graph(matrix, neighbor_func):
    G = nx.DiGraph()
    for i in range(len(matrix)):
         for j in range(len(matrix[0])):
                G.add_node((i,j))
    for node in G.nodes:
        row,col = node
        neighs = neighbor_func(matrix,row,col)
        for neigh in neighs:
            G.add_edge(node,neigh)	
    return G

def neighbors(matrix, row,col):
    n1 = (row+1, col)
    n2 = (row-1, col)
    n3 = (row, col+1)
    n4 = (row, col-1)
    ns = [n1, n2, n3, n4]
    ns = [item for item in ns if not outside_matrix(item, matrix)]
    ns = [item for item in ns if matrix[item] == "."]
    return ns

def outside_matrix(curr, m):
    return (curr[0] < 0 or curr[0] >= len(m)) or (curr[1] < 0 or curr[1] >= len(m))

m = np.full((71,71), ".")


start = (0,0)
goal = (70,70)
for block in blocks[0:1024]:
    m[block] = "#"

G = matrix_to_graph(m, neighbors)
print(len(nx.astar.astar_path(G,start, goal)))

for x in range(1024, len(blocks)):
    for block in blocks[0:x]:
        m[block] = "#"
    G = matrix_to_graph(m, neighbors)
    try: 
        _ = nx.astar.astar_path(G,start, goal)
    except:
        print(blocks[x-1])
        break


