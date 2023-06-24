from typing import Iterable
import networkx as nx
import numpy as np

def find_path(pos, G, return_visit):
    if pos == 'end': return ['end']
    
    adj = list(G.neighbors(pos))
    if len(adj) == 0: return ["DEAD END"]
    
    H = G.copy()
    if pos == 'start':
        H.remove_node(pos)
    else:
        if pos.islower() and return_visit and H.nodes[pos]['visit'] > 0:
            return ['DEAD END']

        H.nodes[pos]['visit'] += 1

        if pos.islower() and H.nodes[pos]['visit'] > 1:
            return_visit = True

        for a in adj:
            if a.islower() and return_visit and H.nodes[a]['visit'] > 0:  
                H.remove_node(a) 
                adj.remove(a)
                
        if len(adj) == 0: return ["DEAD END"]

        if pos.islower() and return_visit: H.remove_node(pos)

    path_tree = [[pos] + find_path(a, H, return_visit) for a in adj]
    return path_tree 

def flatten(tree):
    for elem in tree:
        if isinstance(elem, Iterable) and not isinstance(elem, str):
            yield from flatten(elem)
        else:
            yield elem

if __name__ == "__main__":
    edges = np.genfromtxt("input", delimiter='-', dtype=str)

    G = nx.Graph()
    G.add_edges_from(edges)
    nx.set_node_attributes(G, 0, "visit") 
    liste = find_path('start', G, False)
    #print(liste)
    ends_reached = len([1 for e in flatten(liste) if e == "end"])
    print(ends_reached)