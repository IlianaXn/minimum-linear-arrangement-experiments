# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:47:25 2022

@author: ilmar
"""
import laldebug as lal
import time


def random_normal(path):
    # create graph
    graph = lal.io.read_edge_list('free_tree', path)

    # create generator of random arrangements
    gen_rand_arr = lal.generate.rand_arrangements(graph)

    # random layout
    # get a layout chosen at random and compute its sum of edge lengths
    random_arr = gen_rand_arr.yield_arrangement()
    random_sum = lal.linarr.sum_edge_lengths(graph, random_arr)

    # normal layout
    # create identity arrangement, i.e. u's position is its label,
    # and compute sum of edge lengths
    normal_arr = lal.types.linear_arrangement.identity(graph.get_num_nodes())
    normal_sum = lal.linarr.sum_edge_lengths(graph, normal_arr)
    
    return random_sum, normal_sum

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-input', '--input', required=True, type=str,
                        help='graph file to read')

    args = parser.parse_args()
    path = args.input

    initial_time = time.time()
    random, normal = random_normal(path)
    total_time = time.time() - initial_time

    print('Random layout')
    print(random, total_time)
    print('Normal layout')
    print(normal, total_time)
