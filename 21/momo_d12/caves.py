from typing import Iterable
import networkx as nx
import numpy as np

def find_path(pos, G):
    assert isinstance(pos, str)

    if pos == 'end': return ['end']
    
    adj = list(G.neighbors(pos))
    H = G.copy()
    if pos.islower(): H.remove_node(pos)
    
    if len(adj) == 0: return ["DEAD END"]

    path_tree = [[pos] + find_path(a, H) for a in adj]
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
    liste = find_path('start', G)
    print(liste)
    ends_reached = len([1 for e in flatten(liste) if e == "end"])
    print(ends_reached)