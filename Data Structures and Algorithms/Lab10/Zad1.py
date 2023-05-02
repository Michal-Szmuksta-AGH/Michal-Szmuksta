# NIESKOŃCZONE
import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return str(self.key)


class Edge:
    def __init__(self, capacity, is_residual):
        self.capacity = capacity
        self.residual = capacity
        self.is_residual = is_residual
        self.flow = 0

    def __repr__(self):
        return '{} {} {} {}'.format(self.capacity, self.flow, self.residual, self.is_residual)

    def __str__(self):
        return '{} {} {} {}'.format(self.capacity, self.flow, self.residual, self.is_residual)


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
        # Zmienić przy skierowanym #DONE
        self.list[self.getVertexIdx(vertex1)].append((vertex2, edge))

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
        # Zmienić przy skierowanym #DONE
        for i, (v, e) in enumerate(self.list[self.getVertexIdx(vertex1)]):
            if v == vertex2:
                self.list[self.getVertexIdx(vertex1)].pop(i)
        # for i, (v, e) in enumerate(self.list[self.getVertexIdx(vertex2)]):
        #     if v == vertex1:
        #         self.list[self.getVertexIdx(vertex2)].pop(i)

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
        # Zmienić przy skierowanym #DONE
        size = 0
        for lst in self.list:
            size += len(lst)
        # return int(size / 2)
        return int(size)

    def edges(self):
        # Zmienić przy skierowanym
        lst = []
        black_lst = []
        for i, vl in enumerate(self.list):
            for v, e in vl:
                if v in black_lst:
                    pass
                else:
                    lst.append((self.getVertex(i).capacity, v.capacity))
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
            print(g.getVertex(n_idx), g.getEdge(v, g.getVertex(n_idx)), end=";")
        print()
    print("-------------------")


def bfs(graph, vertex_idx=0):
    queue = [vertex_idx]
    visited = [False] * graph.order()
    parent = [False] * graph.order()
    visited[vertex_idx] = True
    while len(queue) != 0:
        vertex = queue.pop(0)
        for neighbour_idx in graph.neighbours(vertex):
            if visited[neighbour_idx] is False and graph.getEdge(graph.getVertex(vertex),
                                                                 graph.getVertex(neighbour_idx)).residual > 0:
                queue.append(neighbour_idx)
                parent[neighbour_idx] = graph.getVertex(vertex)
                visited[neighbour_idx] = True
            else:
                pass
    return parent


def analysis(graph, start_vertex, end_vertex, parent):
    current_idx = graph.getVertexIdx(end_vertex)
    min_capacity = float('inf')
    if parent[current_idx] is False:
        return 0
    while current_idx is not graph.getVertexIdx(start_vertex):
        parent_idx = graph.getVertexIdx(parent[current_idx])
        neighbours = graph.neighbours(parent_idx)
        for neighbour_idx in neighbours:
            edge = graph.getEdge(graph.getVertex(parent_idx), graph.getVertex(neighbour_idx))
            if neighbour_idx == current_idx and edge is not None and edge.is_residual is False and edge.residual < min_capacity:
                min_capacity = edge.residual
            else:
                pass
        current_idx = parent_idx
    return min_capacity


def augmentation(graph, start_vertex, end_vertex, parent, min_capacity):
    current_idx = graph.getVertexIdx(end_vertex)
    if parent[current_idx] is False:
        return 0
    while current_idx is not graph.getVertexIdx(start_vertex):
        parent_idx = graph.getVertexIdx(parent[current_idx])
        neighbours = graph.neighbours(parent_idx)
        for neighbour_idx in neighbours:
            edge = graph.getEdge(graph.getVertex(parent_idx), graph.getVertex(neighbour_idx))
            if neighbour_idx == current_idx and edge is not None and edge.is_residual is False:
                edge.flow += min_capacity
                edge.residual -= min_capacity
            else:
                pass
        neighbours = graph.neighbours(current_idx)
        for neighbour_idx in neighbours:
            edge = graph.getEdge(graph.getVertex(current_idx), graph.getVertex(neighbour_idx))
            if neighbour_idx == parent_idx and edge is not None and edge.is_residual is True:
                edge.residual += min_capacity
            else:
                pass
        current_idx = parent_idx


def ford_fulkerson(graph, start_vertex, end_vertex):
    parent = bfs(graph)
    current_vertex = end_vertex
    while current_vertex != start_vertex or current_vertex is False:
        current_vertex = parent[graph.getVertexIdx(current_vertex)]
    if current_vertex is False:
        raise Exception
    minimal_flow = analysis(graph, start_vertex, end_vertex, parent)
    while minimal_flow > 0:
        augmentation(graph, start_vertex, end_vertex, parent, minimal_flow)
        parent = bfs(graph)
        minimal_flow = analysis(graph, start_vertex, end_vertex, parent)
    flow_sum = 0
    for neighbour_idx in graph.neighbours(graph.getVertexIdx(end_vertex)):
        edge = graph.getEdge(end_vertex, graph.getVertex(neighbour_idx))
        if edge is not None:
            flow_sum += edge.residual
        else:
            pass
    return flow_sum




def main():
    my_graf_0 = NeighborhoodListGraph()
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    for v1, v2, capacity in graf_0:
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        edge_1 = Edge(capacity, False)
        edge_2 = Edge(0, True)
        my_graf_0.insertVertex(vertex_1)
        my_graf_0.insertVertex(vertex_2)
        my_graf_0.insertEdge(vertex_1, vertex_2, edge_1)
        my_graf_0.insertEdge(vertex_2, vertex_1, edge_2)
    print(ford_fulkerson(my_graf_0, Vertex('s'), Vertex('t')))
    printGraph(my_graf_0)

    my_graf_1 = NeighborhoodListGraph()
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    for v1, v2, capacity in graf_1:
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        edge_1 = Edge(capacity, False)
        edge_2 = Edge(0, True)
        my_graf_1.insertVertex(vertex_1)
        my_graf_1.insertVertex(vertex_2)
        my_graf_1.insertEdge(vertex_1, vertex_2, edge_1)
        my_graf_1.insertEdge(vertex_2, vertex_1, edge_2)
    print(ford_fulkerson(my_graf_1, Vertex('s'), Vertex('t')))
    printGraph(my_graf_1)

    my_graf_2 = NeighborhoodListGraph()
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    for v1, v2, capacity in graf_2:
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        edge_1 = Edge(capacity, False)
        edge_2 = Edge(0, True)
        my_graf_2.insertVertex(vertex_1)
        my_graf_2.insertVertex(vertex_2)
        my_graf_2.insertEdge(vertex_1, vertex_2, edge_1)
        my_graf_2.insertEdge(vertex_2, vertex_1, edge_2)
    print(ford_fulkerson(my_graf_2, Vertex('s'), Vertex('t')))
    printGraph(my_graf_2)

    my_graf_3 = NeighborhoodListGraph()
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    for v1, v2, capacity in graf_3:
        vertex_1 = Vertex(v1)
        vertex_2 = Vertex(v2)
        edge_1 = Edge(capacity, False)
        edge_2 = Edge(0, True)
        my_graf_3.insertVertex(vertex_1)
        my_graf_3.insertVertex(vertex_2)
        my_graf_3.insertEdge(vertex_1, vertex_2, edge_1)
        my_graf_3.insertEdge(vertex_2, vertex_1, edge_2)
    print(ford_fulkerson(my_graf_3, Vertex('s'), Vertex('t')))
    printGraph(my_graf_3)


if __name__ == '__main__':
    main()
