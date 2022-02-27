# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:40:46 2022

@author: ilmar
"""
import laldebug as lal

# create graph
football = lal.io.read_edge_list('free_tree', 'football.txt')

# compute minimum linear arrangement and its sum using Chung's algorithm
min_sum, _ = lal.linarr.min_sum_edge_lengths(football, lal.linarr.algorithms_Dmin.Chung_2)
with open('results.txt', 'w') as f:
    #print('Sum of minimum linear arrangement =', min_sum)
    f.write(f'Sum of minimum linear arrangement = {min_sum}\n')
# help(lal.types.linear_arrangement.from_direct)