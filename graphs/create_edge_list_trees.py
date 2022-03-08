# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:50:30 2022

@author: ilmar
"""
import networkx as nx

import glob

# get all graph files
filenames = glob.glob("./edge_list/*")

# for each file generate a new one as edge list
for file in filenames:
    with open(f'./trees/{file[12:-4]}.txt', 'w') as edge:
        # create graph
        graph = nx.read_edgelist(file)
        
        # keep largest connected component
        graph_nodes = sorted(nx.connected_components(graph), key=len, reverse=True)[0]
        graph = graph.subgraph(graph_nodes)

        # create (minimum spanning) tree
        mst = nx.tree.minimum_spanning_edges(
            graph, algorithm="kruskal", data=False)
        
        tree = nx.Graph(mst)

        # relabel s.t. labels of nodes are integers
        new_tree = nx.convert_node_labels_to_integers(tree, 0, 'sorted')
        edge_list = new_tree.edges
        
        # write to file the edge list
        for node1, node2 in edge_list:
            edge.write(f'{node1} {node2}\n')
