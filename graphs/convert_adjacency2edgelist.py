# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:43:16 2022

@author: ilmar
"""

import glob

# get all graph files
filenames = glob.glob("./adjacency_list/*")

# for each file generate a new one as edge list
for file in filenames:
    with open(file) as adj, open(f'./edge_list/{file[17:-4]}.txt', 'w') as edge:
        content = adj.readlines()
        
        n = int(content[0])
        degrees = list(map(int, content[2].split()))
        neighbors = list(map(int, content[3].split()))
        indices = list(map(int, content[3].split()))
        
        
        for i in range(n):
            # for each node get its neighbors from adjacency list in positions
            # indices[i] to indices[i] + degrees[i]
            for neigh in neighbors[indices[i] : indices[i] + degrees[i]]:
                # add the edge to edge list file
                edge.write(f'{i} {neigh}\n')