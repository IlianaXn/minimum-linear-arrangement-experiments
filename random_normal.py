# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:47:25 2022

@author: ilmar
"""
import laldebug as lal

# create graph
football = lal.io.read_edge_list('free_tree', 'football.txt')

# create generator of random arrangements
gen_rand_arr = lal.generate.rand_arrangements(football)

# random layout
# get a layout chosen at random and compute its sum of edge lengths
random_arr = gen_rand_arr.yield_arrangement()
random_sum = lal.linarr.sum_edge_lengths(football, random_arr)
print('Sum of random arrangement =', random_sum)

# expected sum over all layouts chosen at random
expected_sum = lal.properties.exp_sum_edge_lengths(football)
print('Expected sum of all arrangements =', expected_sum)

# normal layout
# create identity arrangement, i.e. u's position is its label, 
# and compute sum of edge lengths
normal_arr = lal.types.linear_arrangement.identity(football.get_num_nodes())
normal_sum = lal.linarr.sum_edge_lengths(football, normal_arr)
print('Sum of normal arrangement =', normal_sum)