# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:50:30 2022

@author: ilmar
"""
import networkx as nx

# create graph 
football = nx.read_gml(r"football.gml")

# create (minimum spanning) tree
mst = nx.tree.minimum_spanning_edges(football, algorithm="kruskal", data = False)
football = nx.Graph(mst)

# relable s.t. labels of nodes are integers
new_football = nx.convert_node_labels_to_integers(football, 0, 'sorted')
edge_list = new_football.edges

# write to file the edge list
with open('football.txt', 'w') as f:
    for node1, node2 in edge_list:
        f.write(f'{node1} {node2}\n')
