#!/usr/bin/python
# -*- coding: utf-8 -*-
import graphs_1

print(graphs_1.adjmat_to_adjlist([
    [0, 1, 0],
    [0, 0, 1],
    [1, 2, 0]
]))
print(graphs_1.adjmat_to_adjlist([
    [0, 1],
    [0, 0]
]))
print(graphs_1.dfs_recursive({
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}, 1))
print(graphs_1.dfs_iterative({
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}, 1))

print('')
print(graphs_1.is_acyclic({1: [2, 3], 3: [4]}))
print(graphs_1.is_acyclic({1: [2], 2: [3], 3: [1]}))
print(graphs_1.is_acyclic({2: [1, 3], 3: [2]}))
print(graphs_1.is_acyclic({1: [2], 3: [2, 4], 4: [3]}))
print(graphs_1.is_acyclic({1: [2, 3], 2: [4], 3: [4]}))
print(graphs_1.is_acyclic({1: [2, 3], 2: [3]}))
print('')
print(graphs_1.is_acyclic({1: [2], 2: [3], 3: [1, 4]}))
print('')
print(graphs_1.is_acyclic({5: [11], 11: [2, 10, 9], 7: [11, 8], 8: [9], 3: [8, 10], 19: [3]}))
print('')

print(graphs_1.dfs_recursive({1: [2, 3], 2: [4], 3: [4]}, 1))
print(graphs_1.dfs_iterative({1: [2, 3], 2: [4], 3: [4]}, 1))
