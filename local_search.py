# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:27:43 2022

@author: georgekallitsis
"""
import random
import copy
import laldebug as lal
import numpy as np
import time

# swap positions of nodes at pos1 and pos2 positions
def swapPositions2(arrangement, pos1, pos2):
    arrangement[pos1], arrangement[pos2] = arrangement[pos2], arrangement[pos1]
    return arrangement


# swap successively positions of nodes at pos1, pos2 and pos3 positions
def swapPositions3(arrangement, pos1, pos2, pos3):
    arrangement[pos1], arrangement[pos2], arrangement[pos3] = arrangement[pos2], arrangement[pos3], arrangement[pos1]
    return arrangement


# find the neighborhood of the given permutation by swapping positions of two random nodes
def neighbor2(arrangement):
    # save given arrangement so it doesn't get affected by permutations
    initial = copy.deepcopy(arrangement)

    # number of neighbor arrangements (at most 5000...)
    length = 0

    # neighborhood of arrangements
    result = []

    length_arr = len(arrangement)

    # flag indicates when to stop
    flag = True

    # choose nodes to swap positions
    for i in range(length_arr):
        if not flag:
            break
        for j in range(i + 1, length_arr):
            if not flag:
                break

            new_arrangement = swapPositions2(initial, i, j)
            result.append(new_arrangement)

            initial = copy.deepcopy(arrangement)

            length += 1

            if length == 5000:
                flag = False
                
    # shuffle neighborhood in order to choose at random
    random.shuffle(result)
    return result


# find the neighborhood of the given permutation by swapping adjacent nodes
def neighbor2b(arrangement, rt):
    # save given arrangement so it doesn't get affected by permutations
    initial = copy.deepcopy(arrangement)

    # number of neighbor arrangements (at most 5000...)
    length = 0

    # neighborhood of arrangements
    aux = set()

    length_arr = len(arrangement)

    # flag indicates when to stop
    flag = True

    for i in range(length_arr):
        if not flag:
            break

        # get the neighbours of each node and swap labels with them
        adjacent = rt.get_neighbours(i)
        
        for j in adjacent:
            if not flag:
                break
            new_arrangement = swapPositions2(initial, i, j)
            
            # only if new arrangement doesn't exist in our result, we add it
            if tuple(new_arrangement) not in aux:
                aux.add(tuple(new_arrangement))

                initial = copy.deepcopy(arrangement)

                length += 1

                if length == 5000:
                    flag = False
    result = []
    for i in aux:
        result.append(list(i))
    
    # shuffle neighborhood in order to choose at random
    random.shuffle(result)
    return result

# find the neighborhood of the given permutation by swapping positions of three random nodes
def neighbor3(arrangement):
    # save given arrangement so it doesn't get affected by permutations
    initial = copy.deepcopy(arrangement)

    # number of neighbor arrangements (at most 5000...)
    length = 0

    # neighborhood of arrangements
    result = []

    length_arr = len(arrangement)

    # flag indicates when to stop
    flag = True

    # choose nodes to swap positions
    for i in range(length_arr):
        if not flag:
            break
        for j in range(i + 1, length_arr):
            if not flag:
                break
            for k in range(j + 1, length_arr):
                if not flag:
                    break

                new_arrangement = swapPositions3(initial, i, j, k)
                result.append(new_arrangement)

                initial = copy.deepcopy(arrangement)

                length += 1

                if length == 5000:
                    flag = False

    # shuffle neighborhood in order to choose at random
    random.shuffle(result)
    return result


def local_search(rt, version):

    # stopping criterion
    max_tries = 5000

    # when to stop, at most max_times
    current_tries = 0

    # random initial permutation
    current_permutation = list(
        map(int, np.random.permutation(rt.get_num_nodes())))

    arrangement_lal = lal.types.linear_arrangement(rt.get_num_nodes())

    # adjust arrangement to arrangement found before
    for i in range(len(current_permutation)):
        arrangement_lal.assign(i, current_permutation[i])

    # sum of lenth of edges for random arrangement
    current_result = lal.linarr.sum_edge_lengths(rt, arrangement_lal)

    # which neighbor arrangement to check
    position = 0

    if version == '2':
        neighborhood = neighbor2(current_permutation)

        while current_tries < max_tries:
            current_tries += 1

            # choose neighbor arrangement
            next_arrangement = neighborhood[position]

            # adjust arrangement to arrangement found before
            arrangement_lal = lal.types.linear_arrangement(rt.get_num_nodes())
            for i in range(len(next_arrangement)):
                arrangement_lal.assign(i, next_arrangement[i])

            # compute sum of lenth of edges
            result = lal.linarr.sum_edge_lengths(rt, arrangement_lal)
            if result < current_result:

                # choose smaller result
                current_result = result
                current_permutation = next_arrangement

                # since we changed current permutation, find new neighborhood of arrangements
                neighborhood = neighbor2(current_permutation)
                current_tries = 0

                # initialize position
                position = 0
            else:
                # check next neighbor
                position += 1
                if position == len(neighborhood) - 1:
                    break
    elif version == '2b':
        neighborhood = neighbor2b(current_permutation, rt)

        while current_tries < max_tries:
            current_tries += 1

            # choose neighbor arrangement
            next_arrangement = neighborhood[position]

            # adjust arrangement to arrangement found before
            arrangement_lal = lal.types.linear_arrangement(rt.get_num_nodes())
            for i in range(len(next_arrangement)):
                arrangement_lal.assign(i, next_arrangement[i])

            # compute sum of lenth of edges
            result = lal.linarr.sum_edge_lengths(rt, arrangement_lal)
            if result < current_result:

                # choose smaller result
                current_result = result
                current_permutation = next_arrangement

                # since we changed current permutation, find new neighborhood of arrangements
                neighborhood = neighbor2b(current_permutation, rt)
                current_tries = 0

                # initialize position
                position = 0
            else:
                # check next neighbor
                position += 1
                if position == len(neighborhood) - 1:
                    break
    elif version == '3':
        neighborhood = neighbor3(current_permutation)

        while current_tries < max_tries:
            current_tries += 1

            # choose neighbor arrangement
            next_arrangement = neighborhood[position]

            # adjust arrangement to arrangement found before
            arrangement_lal = lal.types.linear_arrangement(rt.get_num_nodes())
            for i in range(len(next_arrangement)):
                arrangement_lal.assign(i, next_arrangement[i])

            # compute sum of lenth of edges
            result = lal.linarr.sum_edge_lengths(rt, arrangement_lal)
            if result < current_result:

                # choose smaller result
                current_result = result
                current_permutation = next_arrangement

                # since we changed current permutation, find new neighborhood of arrangements
                neighborhood = neighbor3(current_permutation)
                current_tries = 0

                # initialize position
                position = 0
            else:
                # check next neighbor
                position += 1
                if position == len(neighborhood) - 1:
                    break
    else:
        print("Version should be 2 or 2b or 3 for now...")
    return current_result, current_permutation

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-input', '--input', required=True, type=str, 
                        help='graph file to read')

    args = parser.parse_args()
    path = args.input
    
    # create graph
    graph = lal.io.read_edge_list('free_tree', path)
    

    
    print('Local search v2b')
    initial_time = time.time()
    D2b, _ = local_search(graph, '2b')
    total_time = time.time() - initial_time
    print(D2b, total_time)
    
    print('Local search v2')
    initial_time = time.time()
    D2, _ = local_search(graph, '2')
    total_time = time.time() - initial_time
    print(D2, total_time)
    
    print('Local search v3')
    initial_time = time.time()
    D3, _ = local_search(graph, '3')
    total_time = time.time() - initial_time
    print(D3, total_time)