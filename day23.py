import networkx as nx
edge_pairs = [item.strip() for item in open("day23.txt").readlines()]

G = nx.Graph()
for edge_pair in edge_pairs:
    u,v = edge_pair.split("-")
    G.add_edge(u,v)

print(",".join(sorted(sorted(nx.clique.find_cliques(G), key = lambda x: len(x))[-1])))
#print(",".join(sorted(max_clique)))