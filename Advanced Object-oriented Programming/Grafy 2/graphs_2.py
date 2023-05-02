# Michał Szmuksta 406376
# !/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Set, Dict, NamedTuple
from enum import Enum, auto
import networkx as nx

# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
EdgeID = int
Distance = int

# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]


class Color(Enum):
    WHITE = auto()
    GREY = auto()
    BLACK = auto()


class Distancetuple(NamedTuple):
    VertexID: int
    Distance: int


def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    # Ustawienie wszystkich elementów na kolor biały
    Colordict = {}
    for keys in adjlist.keys():
        Colordict[keys] = Color.WHITE
        for values in adjlist[keys]:
            Colordict[values] = Color.WHITE

    # Zainicjalizowanie kolejki Q krotką dystansu wierzchołka startowego oraz zbioru wynikowego
    Colordict[start_vertex_id] = Color.GREY
    Queue = [Distancetuple(start_vertex_id, 0)]
    Neighborsset = set()

    # Analiza sąsiadów wierzchołków z kolejki
    while Queue:
        u = Queue.pop(0)
        if u.Distance <= max_distance and u.VertexID != start_vertex_id:
            Neighborsset.add(u.VertexID)
        if u.Distance > max_distance:
            return Neighborsset
        if u.VertexID in adjlist.keys():
            for v in adjlist[u.VertexID]:
                if Colordict[v] == Color.WHITE:
                    Colordict[v] = Color.GREY
                    Queue.append(Distancetuple(v, u.Distance + 1))
            Colordict[u.VertexID] = Color.BLACK
    return Neighborsset
