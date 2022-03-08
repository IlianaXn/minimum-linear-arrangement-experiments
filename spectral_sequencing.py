# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:01:19 2022

@author: ilmar
"""
import networkx as nx
import numpy as np
import laldebug as lal
import time

def spectral_sequencing(path):
    # read graph
    graph = nx.read_edgelist(path, nodetype=int)
    
    nodelist = sorted(graph.nodes)
    
    # compute Laplacian matrix
    L = nx.normalized_laplacian_matrix(graph, nodelist)
    
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
    graph_lal = lal.io.read_edge_list('free_tree', path)
    
    # identity arrangement of graph
    arrangement_lal = lal.types.linear_arrangement(graph_lal.get_num_nodes())
    
    # adjust arrangement to arrangement found before
    for i in range(len(arrangement)):
        arrangement_lal.assign(arrangement[i], i)
        
    # compute sum of edge lengths
    spectral_sum = lal.linarr.sum_edge_lengths(graph_lal, arrangement_lal)
    
    return spectral_sum
    
    ''' # without lal library
    
    # create arrangement dictionary s.t. d[v] = u means that v's position is u
    arrangement_dict = dict()
    
    for i in range(len(arrangement)):
        arrangement_dict[arrangement[i]] = i
        
    # compute all edge lengths according to arrangement
    sum_edges = 0
    for edge in graph.edges:
        sum_edges += abs(arrangement_dict[edge[0]] - arrangement_dict[edge[1]])
        
    print('Sum of arrangement =', sum_edges)
    '''

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-input', '--input', required=True, type=str, 
                        help='graph file to read')

    args = parser.parse_args()
    path = args.input
    
    print('Spectral sequencing')
    initial_time = time.time()
    min_sum = spectral_sequencing(path)
    total_time = time.time() - initial_time
    print(min_sum, total_time)