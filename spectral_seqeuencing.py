# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:01:19 2022

@author: ilmar
"""
import networkx as nx
import numpy as np
import laldebug as lal

# read graph
football = nx.read_edgelist('football.txt', nodetype=int)

nodelist = sorted(football.nodes)

# compute Laplacian matrix
L = nx.normalized_laplacian_matrix(football, nodelist)

# compute Laplacian eigenvalues and eigenvectors
val, vec = np.linalg.eig(L.A)

# get traspose matrix of vec s.t. vec[i] corresponds to val[i]
vec = np.transpose(vec)

# sort eigenvectors according to eigenvalues
sorted_vec = [vector for _, vector in sorted(zip(val, vec), key=lambda x: x[0])]

# choose eigenvector corresponding to second smallest eigenvalue
vec2 = sorted_vec[1]

# match arrangement with vector position
arrangement = [node for _, node in sorted(zip(vec2, nodelist), key=lambda x: x[0])]

# create graph with lal library
football_lal = lal.io.read_edge_list('free_tree', 'football.txt')

# identity arrangement of graph
arrangement_lal = lal.types.linear_arrangement(football_lal.get_num_nodes())

# adjust arrangement to arrangement found before
for i in range(len(arrangement)):
    arrangement_lal.assign(arrangement[i], i)
    
# compute sum of edge lengths
spectral_sum = lal.linarr.sum_edge_lengths(football_lal, arrangement_lal)
with open('results.txt', 'a') as f:
    #print('Sum of spectral sequencing arrangement =', spectral_sum)
    f.write(f'Sum of spectral sequencing arrangement = {spectral_sum}\n')

''' # without lal library

# create arrangement dictionary s.t. d[v] = u means that v's position is u
arrangement_dict = dict()

for i in range(len(arrangement)):
    arrangement_dict[arrangement[i]] = i
    
# compute all edge lengths according to arrangement
sum_edges = 0
for edge in football.edges:
    sum_edges += abs(arrangement_dict[edge[0]] - arrangement_dict[edge[1]])
    
print('Sum of arrangement =', sum_edges)
'''