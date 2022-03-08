# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:40:46 2022

@author: ilmar
"""
import laldebug as lal
import time


def ground_truth(path, shiloach):
    # create graph
    graph = lal.io.read_edge_list('free_tree', path)
    
    if shiloach:
        # compute minimum linear arrangement and its sum using Chung's algorithm
        min_sum, _ = lal.linarr.min_sum_edge_lengths(graph, lal.linarr.algorithms_Dmin.Chung_2)
    else:
        min_sum, _ = lal.linarr.min_sum_edge_lengths(graph, lal.linarr.algorithms_Dmin.Shiloach)
    return min_sum

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-input', '--input', required=True, type=str, 
                        help='graph file to read')

    args = parser.parse_args()
    path = args.input
    
    print(f'{path[13:-4]}')
    
    
    print('Shiloach algorithm')
    initial_time = time.time()
    min_sum = ground_truth(path, True)
    total_time = time.time() - initial_time
    print(min_sum, total_time)
    
    print('Chung algorithm')
    initial_time = time.time()
    min_sum = ground_truth(path, False)
    total_time = time.time() - initial_time
    print(min_sum, total_time)