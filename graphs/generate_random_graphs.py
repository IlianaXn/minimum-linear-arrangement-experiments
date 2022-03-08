# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:21:32 2022

@author: ilmar
"""

import networkx as nx

# generate random graphs following Gilbert model
A1 = nx.gnp_random_graph(n=500, p=0.02)
A2 = nx.gnp_random_graph(n=500, p=0.04)

# generate random geometric graphs
G1 = nx.random_geometric_graph(n=500, radius=0.075)
G2 = nx.random_geometric_graph(n=500, radius=0.125)

# generate random graph following Erdos-Renyi model
A3 = nx.gnm_random_graph(n=500, m=800)

# save graphs to files
nx.write_edgelist(A1, './edge_list/randomA1.txt', data=False)
nx.write_edgelist(A2, './edge_list/randomA2.txt', data=False)
nx.write_edgelist(G1, './edge_list/randomG1.txt', data=False)
nx.write_edgelist(G2, './edge_list/randomG2.txt', data=False)
nx.write_edgelist(A3, './edge_list/randomA3.txt', data=False)
