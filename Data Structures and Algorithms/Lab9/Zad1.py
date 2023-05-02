# SKOŃCZONE
import graf_mst
import numpy as np


class Vertex:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return str(self.key)

    def show_color(self):
        return self.color

    def change_color(self, color):
        self.color = color


class Edge:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return str(self.key)


class NeighborhoodListGraph:
    def __init__(self):
        self.list = []
        self.dict = {}

    def insertVertex(self, vertex):
        if vertex in self.dict.keys():
            pass
        else:
            self.dict[vertex] = len(self.list)
            self.list.append([])

    def insertEdge(self, vertex1, vertex2, edge):
        # Zmienić przy skierowanym
        sem = 0
        for i, (v, k) in enumerate(self.list[self.getVertexIdx(vertex1)]):
            if v == vertex2:
                sem = 1
                self.list[self.getVertexIdx(vertex1)][i] = (v, edge)
                break
        if sem == 0:
            self.list[self.getVertexIdx(vertex1)].append((vertex2, edge))
        sem = 0
        for i, (v, k) in enumerate(self.list[self.getVertexIdx(vertex2)]):
            if v == vertex1:
                sem = 1
                self.list[self.getVertexIdx(vertex2)][i] = (v, edge)
                break
        if sem == 0:
            self.list[self.getVertexIdx(vertex2)].append((vertex1, edge))

    def deleteVertex(self, vertex):
        for vl, el in self.list[self.getVertexIdx(vertex)]:
            for i, (v, e) in enumerate(self.list[self.getVertexIdx(vl)]):
                if v == vertex:
                    self.list[self.getVertexIdx(vl)].pop(i)
        self.list.pop(self.getVertexIdx(vertex))
        index = self.dict.pop(vertex)
        for k, v in self.dict.items():
            if v >= index:
                self.dict[k] -= 1

    def deleteEdge(self, vertex1, vertex2):
        # Zmienić przy skierowanym
        for i, (v, e) in enumerate(self.list[self.getVertexIdx(vertex1)]):
            if v == vertex2:
                self.list[self.getVertexIdx(vertex1)].pop(i)
        for i, (v, e) in enumerate(self.list[self.getVertexIdx(vertex2)]):
            if v == vertex1:
                self.list[self.getVertexIdx(vertex2)].pop(i)

    def getEdge(self, vertex1, vertex2):
        for v, e in self.list[self.getVertexIdx(vertex1)]:
            if v == vertex2:
                return e
        return None

    def getVertexIdx(self, vertex):
        return self.dict.get(vertex)

    def getVertex(self, vertex_idx):
        for k, v in self.dict.items():
            if v == vertex_idx:
                return k

    def neighbours(self, vertex_idx):
        lst = []
        for v, e in self.list[vertex_idx]:
            lst.append(self.getVertexIdx(v))
        return lst

    def order(self):
        return len(self.dict)

    def size(self):
        # Zmienić przy skierowanym
        size = 0
        for lst in self.list:
            size += len(lst)
        return int(size / 2)

    def edges(self):
        # Zmienić przy skierowanym
        lst = []
        black_lst = []
        for i, vl in enumerate(self.list):
            for v, e in vl:
                if v in black_lst:
                    pass
                else:
                    lst.append((self.getVertex(i).key, v.key))
            black_lst.append(self.getVertex(i))
        return lst


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for n_idx in nbrs:
            print(g.getVertex(n_idx), g.getEdge(v, g.getVertex(n_idx)).key, end=";")
        print()
    print("-------------------")


def prime(input_graph, starting_vertex):
    intree = [0 for i in range(input_graph.order())]
    distance = [float('inf') for i in range(input_graph.order())]
    parent = [-1 for i in range(input_graph.order())]

    MST = NeighborhoodListGraph()
    for v1, v2 in input_graph.edges():
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        MST.insertVertex(vertex_1)
        MST.insertVertex(vertex_2)

    s = 0
    v = starting_vertex
    v_idx = input_graph.getVertexIdx(starting_vertex)
    while intree[v_idx] == 0:
        intree[v_idx] = 1
        surrounding = input_graph.neighbours(v_idx)
        for neighbour_idx in surrounding:
            edge = input_graph.getEdge(v, input_graph.getVertex(neighbour_idx))
            if edge.key < distance[neighbour_idx] and intree[neighbour_idx] == 0:
                distance[neighbour_idx] = edge.key
                parent[neighbour_idx] = v_idx

        minimal_distance = float('inf')
        for w1, w2 in input_graph.edges():
            w1_idx = input_graph.getVertexIdx(Vertex(w1))
            w2_idx = input_graph.getVertexIdx(Vertex(w2))
            if intree[w1_idx] == 0 and distance[w1_idx] < minimal_distance:
                minimal_distance = distance[w1_idx]
                v_idx = w1_idx
                v = input_graph.getVertex(v_idx)
            if intree[w2_idx] == 0 and distance[w2_idx] < minimal_distance:
                minimal_distance = distance[w2_idx]
                v_idx = w2_idx
                v = input_graph.getVertex(v_idx)
        if minimal_distance != float('inf'):
            MST.insertEdge(input_graph.getVertex(v_idx), input_graph.getVertex(parent[v_idx]), Edge(minimal_distance))
            s += minimal_distance

    return MST, s


def main():
    graph = NeighborhoodListGraph()
    for v1, v2, e in graf_mst.graf:
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        edge = Edge(e)
        graph.insertVertex(vertex_1)
        graph.insertVertex(vertex_2)
        graph.insertEdge(vertex_1, vertex_2, edge)
    mst, sum = prime(graph, graph.getVertex(0))
    printGraph(mst)


if __name__ == '__main__':
    main()
