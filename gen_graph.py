#!/usr/bin/env python

try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx

def foo(n, men, women):
    G=nx.Graph()
    # Add nodes corresponding to men, women
    B.add_nodes_from(map(self.pid, mens), bipartite=0)
    B.add_nodes_from(map(self.pid, womens), bipartite=1)
    pos = {}
    # Map men and women to positions
    for i in range(len(mens)):
        pos[men[i].pid] = (0, i)
        pos[women[i].pid] = (1, i)
    nx.draw(G, pos)
    plt.savefig("test.png")
    plt.show()
        
