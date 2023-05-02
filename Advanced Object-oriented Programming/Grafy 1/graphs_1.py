# Michał Szmuksta 406376
# !/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist: Dict[int, List[int]] = {}
    for row_index, row in enumerate(adjmat):
        adjlist.update({row_index + 1: []})
        for column_index, column in enumerate(adjmat[row_index]):
            for i in range(0, column):
                adjlist[row_index + 1].append(column_index + 1)
        if not adjlist[row_index + 1]:
            adjlist.pop(row_index + 1)
    return adjlist


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    def dfs_recursive_inplace(D: Dict[int, List[int]], v: int, visited_inplace: List[int]):
        visited_inplace.append(v)
        for u in G[v]:
            if u not in visited_inplace and u in G.keys():
                dfs_recursive_inplace(D, u, visited_inplace)

    visited: List[int] = []
    dfs_recursive_inplace(G, s, visited)
    return visited


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    S: List[int] = [s]
    visited: List[int] = []
    while len(S) != 0:
        v = S[-1]
        S.pop(-1)
        if v not in visited and v in G.keys():
            visited.append(v)
            for u in G[v][::-1]:
                S.append(u)
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:
    def is_acyclic_recursive(G_r: Dict[int, List[int]], s, visited_r: List[int]) -> bool:
        visited_r.append(s)
        for a in G_r[s]:
            if a in visited_r:
                return False
            if a in G_r.keys() and not is_acyclic_recursive(G_r, a, visited_r):
                return False
        return True

    for i in G.keys():
        visited = []
        if not is_acyclic_recursive(G, i, visited):
            return False
    return True
