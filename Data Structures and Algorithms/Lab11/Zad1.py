# SKOŃCZONE
from copy import copy

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
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return str(self.key)

    def __mul__(self, other):
        return self.key * other.key

    def __rmul__(self, other):
        return self.key * other

    def __eq__(self, other):
        return self.key == other.key


class NeighborhoodMatrixGraph:
    def __init__(self):
        self.matrix = []
        self.dict = {}

    def insertVertex(self, vertex):
        if vertex in self.dict.keys():
            pass
        else:
            self.dict[vertex] = len(self.matrix)
            for i in self.matrix:
                i.append(0)
            if len(self.matrix) == 0:
                self.matrix.append([0])
            else:
                self.matrix.append([0] * (self.dict[vertex] + 1))

    def insertEdge(self, vertex1, vertex2, edge):
        # Zmienić przy skierowanym
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = edge
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = edge

    def deleteVertex(self, vertex):
        self.matrix.pop(self.getVertexIdx(vertex))
        for row in self.matrix:
            row.pop(self.getVertexIdx(vertex))
        index = self.dict.pop(vertex)
        for k, v in self.dict.items():
            if v >= index:
                self.dict[k] -= 1

    def deleteEdge(self, vertex1, vertex2):
        # Zmienić przy skierowanym
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = 0
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = 0

    def getVertexIdx(self, vertex):
        return self.dict.get(vertex)

    def getVertex(self, vertex_idx):
        for k, v in self.dict.items():
            if v == vertex_idx:
                return k

    def neighbours(self, vertex_idx):
        idx_list = []
        for i, el in enumerate(self.matrix[vertex_idx]):
            if isinstance(el, Edge):
                idx_list.append(i)
        return idx_list

    def order(self):
        return len(self.dict)

    def size(self):
        # Zmienić przy skierowanym
        size = 0
        k = 0
        for i in self.matrix:
            for j in i[k:]:
                if j != 0:
                    size += 1
            k += 1
        return size

    def edges(self):
        # Zmienić przy skierowanym
        lst = []
        k = 0
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row[k:]):
                if col != 0:
                    lst.append((self.getVertex(i).key, self.getVertex(j + k).key))
            k += 1
        return lst

    def getMatrix(self):
        matrix = np.zeros((len(self.matrix), len(self.matrix)))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if isinstance(self.matrix[i][j], Edge):
                    matrix[i][j] = 1
        return matrix

    # def getEdges(self, vertex_idx):
    #     edges_list = []
    #     for el in self.matrix[vertex_idx]:
    #         if el != 0:
    #             edges_list.append(el)
    #     return edges_list


def ullman(used_columns, current_row, G, P, M, no_solutions=0, no_recursion=0):
    Y, X = M.shape
    if current_row == Y:
        if (P == M @ (M @ G).T).all():
            return no_solutions + 1, no_recursion
        else:
            return no_solutions, no_recursion

    M_copy = copy(M)

    for c in range(X):
        if c not in used_columns:
            M_copy[current_row][:].fill(0)
            M_copy[current_row][c] = 1
            used_columns.append(c)
            no_solutions, no_recursion = ullman(used_columns, current_row + 1, G, P, M_copy, no_solutions, no_recursion + 1)
            used_columns.pop(used_columns.index(c))
    return no_solutions, no_recursion


def ullman2(used_columns, current_row, G, P, M, M0, no_solutions=0, no_recursion=0):
    Y, X = M.shape
    if current_row == Y:
        if (P == M @ (M @ G).T).all():
            return no_solutions + 1, no_recursion
        else:
            return no_solutions, no_recursion

    M_copy = copy(M)

    for c in range(X):
        if c not in used_columns:
            if M0[current_row][c] == 1:
                M_copy[current_row][:].fill(0)
                M_copy[current_row][c] = 1
                used_columns.append(c)
                no_solutions, no_recursion = ullman2(used_columns, current_row + 1, G, P, M_copy, M0, no_solutions, no_recursion + 1)
                used_columns.pop(used_columns.index(c))
    return no_solutions, no_recursion


def prune(M, G, P):
    M_copy = copy(M)
    Y, X = M_copy.shape
    while True:
        changed = 0
        for i in range(Y):
            for j in range(X):
                if M_copy[i][j] == 1:
                    G_neighbours = G.neighbours(j)
                    P_neighbours = P.neighbours(i)
                    sem = 0
                    for x in P_neighbours:
                        for y in G_neighbours:
                            if M_copy[x][y] == 1:
                                sem = 1
                    if sem == 0:
                        changed = 1
                        M_copy[i][j] = 0
        if changed == 0:
            break
    for i in M_copy[:Y - 1]:
        if np.sum(i) == 0:
            return M_copy, True
    return M_copy, False


def ullman3(used_columns, current_row, G, my_G, P, my_P, M, M0, no_solutions=0, no_recursion=0):
    Y, X = M.shape
    if current_row == Y:
        if (P == M @ (M @ G).T).all():
            return no_solutions + 1, no_recursion
        else:
            return no_solutions, no_recursion

    M_copy = copy(M)
    if current_row == Y - 1:
        M_copy, sem = prune(M_copy, my_G, my_P)
        if sem:
            return no_solutions, no_recursion

    for c in range(X):
        if c not in used_columns:
            if M0[current_row][c] == 1:
                M_copy[current_row][:].fill(0)
                M_copy[current_row][c] = 1
                used_columns.append(c)
                no_solutions, no_recursion = ullman3(used_columns, current_row + 1, G, my_G, P, my_P, M_copy, M0, no_solutions, no_recursion + 1)
                used_columns.pop(used_columns.index(c))
    return no_solutions, no_recursion


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    my_graph_G = NeighborhoodMatrixGraph()
    for v1, v2, e in graph_G:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        edge = Edge(e)
        my_graph_G.insertVertex(vertex1)
        my_graph_G.insertVertex(vertex2)
        my_graph_G.insertEdge(vertex1, vertex2, edge)
    G_matrix = my_graph_G.getMatrix()

    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    my_graph_P = NeighborhoodMatrixGraph()
    for v1, v2, e in graph_P:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        edge = Edge(e)
        my_graph_P.insertVertex(vertex1)
        my_graph_P.insertVertex(vertex2)
        my_graph_P.insertEdge(vertex1, vertex2, edge)
    P_matrix = my_graph_P.getMatrix()

    M = np.full((P_matrix.shape[0], G_matrix.shape[0]), 0)
    print(ullman([], 0, G_matrix, P_matrix, M))

    M = np.full((P_matrix.shape[0], G_matrix.shape[0]), 0)
    M0 = np.full((P_matrix.shape[0], G_matrix.shape[0]), 0)
    Y, X = M0.shape
    for i in range(Y):
        for j in range(X):
            if len(my_graph_P.neighbours(i)) <= len(my_graph_G.neighbours(j)):
                M0[i][j] = 1
    print(ullman2([], 0, G_matrix, P_matrix, M, M0))

    M = np.full((P_matrix.shape[0], G_matrix.shape[0]), 0)
    print(ullman3([], 0, G_matrix, my_graph_G, P_matrix, my_graph_P, M, M0))

    # x, sem = prune(np.array([[0,1,0,0,0,0],
    #                          [0,0,0,0,0,1],
    #                          [0,0,0,0,0,0]]), my_graph_G, my_graph_P)
    # print(x, sem)


if __name__ == '__main__':
    main()
