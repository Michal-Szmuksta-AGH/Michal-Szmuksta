#skonczone
import numpy as np
from copy import deepcopy

global iteration, number_of_isomorphisms

class Vertex:
    def __init__(self, name):
        self.name = name
        self.color = None

    def __hash__(self):
        return hash(self.name)

class Edge:
    def __init__(self, point1, point2, edge):
        self.point1 = point1
        self.point2 = point2
        self.weight = edge


class Matrix:
    def __init__(self):
        self.Matrix = []
        self.map = {}

    def map_print(self):
        print(self.map)
        return

    def insertVertex(self, vertex):
        if self.map == {}:
            self.map[vertex.name] = 0
        elif vertex.name not in self.map.keys():
            self.map[vertex.name] = max(self.map.values()) + 1
        size = len(self.map)
        if size > len(self.Matrix):
            new_matrix = []
            for i in range(size):
                new_matrix.append([])
                for j in range(size):
                    try:
                        new_matrix[i].append(self.Matrix[i][j])
                    except:
                        new_matrix[i].append(0)
            self.Matrix = new_matrix

    def insertEdge(self, vertex1, vertex2, edge):#
        if vertex1.name not in self.map.keys():
            self.insertVertex(vertex1)
        if vertex2.name not in self.map.keys():
            self.insertVertex(vertex2)
        self.Matrix[self.map[vertex1.name]][self.map[vertex2.name]] = edge #edge.weight
        self.Matrix[self.map[vertex2.name]][self.map[vertex1.name]] = edge

    def deleteEdge(self, vertex1, vertex2):#, edge = None):
        self.Matrix[self.map[vertex1.name]][self.map[vertex2.name]] = 0 #edge.weight
        self.Matrix[self.map[vertex2.name]][self.map[vertex1.name]] = 0


    def deleteVertex(self, vertex):
        Found = False
        prev = None
        i = 0
        for id, el in enumerate(self.map.keys()):
            if Found:
                self.map[el] = self.map[prev] + i
                i += 1
            if el == vertex.name:
                needed = el
                Found = True
                mappedvertex = self.map[el]
            prev = el

        if not Found:
            return
        del self.map[needed]

        new_matrix = [[0 for j in range(len(self.map))] for i in range(len(self.map))]

        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if i < mappedvertex <= j:
                    new_matrix[i][j] = self.Matrix[i][j + 1]
                elif i >= mappedvertex > j:
                    new_matrix[i][j] = self.Matrix[i + 1][j]
                elif i < mappedvertex and j < mappedvertex:
                    new_matrix[i][j] = self.Matrix[i][j]
                elif i >= mappedvertex and j >= mappedvertex:
                    new_matrix[i][j] = self.Matrix[i + 1][j + 1]

        self.Matrix = new_matrix

    def getVertexIdx(self, vertex):
        return self.map[vertex]

    def getVertex(self, vertex_idx):
        for key, value in self.map.items():
            if value == vertex_idx:
                return key
    def neighbors(self, vertex_idx):
        neigh = [id for id, x in enumerate(self.Matrix[vertex_idx]) if x != 0]
        list_ne = []
        for key, value in self.map.items():
            if value in neigh:
                list_ne.append(key)
        return list_ne

    def order(self):
        return len(self.map)

    def size(self):
        y = [x for x in self.Matrix if x != 0]
        return len(y)/2

    def __str__(self):
        string = ""
        for el in self.Matrix:
            string += str(el) + "\n"
        return string

    def list_of_neighbors(self):
        list_of = [[(list(self.map.keys())[list(self.map.values()).index(i)], list(self.map.keys())[list(self.map.values()).index(j)]) for j in range(len(self.map)) if self.Matrix[i][j] != 0] for i in range(len(self.map))]
        final_list = []
        [final_list.extend(el) for el in list_of]
        return final_list

def isomorphism(M, P, G):
    if np.array_equal(P, np.dot(M, np.dot(M, G).T)):
        return True
    return False

def puring(M, P, G):
    # [0,1,0,0,0,0]
    # [0,0,0,0,1,0]
    # [0,0,0,0,0,1]

    # [0,0,0,0,0,0]
    # [1,0,1,1,0,0]
    # [1,0,1,1,0,0]
    y = np.where(M[0] == 1)[0]
    if len(y) > 0:
        newP = np.reshape(P[0], (3,1))
        new_mat = np.dot(newP, G[y])
        for i in range(1, M.shape[0]):
            y = np.where(M[i] == 1)[0]
            if not len(y):
                return True
            if new_mat[i, y] != 1:
                return False
        return True
    return True

def ullman(unused_colums, current_row, G : np.array, P : np.array, M : np.array):
    global iteration, number_of_isomorphisms
    iteration += 1
    if current_row == M.shape[0]:
        if isomorphism(M, P, G):
            number_of_isomorphisms += 1
            return
        else:
            return
    M_copy = deepcopy(M)
    for c in unused_colums:
        M_copy[current_row, c] = 1
        unused_colums.remove(c)
        ullman(unused_colums, current_row + 1, G, P, M_copy)
        unused_colums.append(c)
        M_copy[current_row, c] = 0
        unused_colums.sort()#bez sort zwraca inny równeiż poprawny wynik[[0,0,0,0,0,1],[0,0,0,1,0,0],[0,0,0,0,1,0]]
    return iteration, number_of_isomorphisms

def ullman_iter(unused_colums, current_row, G : np.array, P : np.array, M : np.array):
    num_of_iter = 0
    num_of_found_isomorphisms = 0
    X, Y = M.shape
    for i in range(Y):
        for j in range(Y):
            for k in range(Y):
                if i != j != k != i:
                    M = np.zeros((X, Y))
                    M[0, i] = 1
                    M[1, j] = 1
                    M[2, k] = 1
                    if isomorphism(M, P, G):
                        num_of_found_isomorphisms += 1
                    num_of_iter += 1
    return num_of_iter, num_of_found_isomorphisms
    pass

def ullman1(unused_colums, current_row, G : np.array, P : np.array, M : np.array, M0 : np.array):
    global iteration, number_of_isomorphisms
    iteration += 1
    if current_row == M.shape[0]:
        if isomorphism(M, P, G):
            number_of_isomorphisms += 1
            return
        else:
            return
    M_copy = deepcopy(M)
    for c in unused_colums:
        if M0[current_row, c] == 1:
            unused_colums.remove(c)
            M_copy[current_row, c] = 1
            ullman1(unused_colums, current_row + 1, G, P, M_copy, M0)
            M_copy[current_row, c] = 0
            unused_colums.append(c)
            unused_colums.sort()#bez sort zwraca inny równeiż poprawny wynik[[0,0,0,0,0,1],[0,0,0,1,0,0],[0,0,0,0,1,0]]
    return iteration, number_of_isomorphisms

def ullman_iter1(unused_colums, current_row, G : np.array, P : np.array, M : np.array, M0 : np.array):
    num_of_iter = 0
    num_of_found_isomorphisms = 0
    X, Y = M.shape
    for i in range(Y):
        for j in range(Y):
            for k in range(Y):
                if i != j != k != i and M0[0, i] == M0[1, j] == M0[2, k] == 1:
                    M = np.zeros((X, Y))
                    M[0, i] = 1
                    M[1, j] = 1
                    M[2, k] = 1
                    if isomorphism(M, P, G):
                        num_of_found_isomorphisms += 1
                    num_of_iter += 1
    return num_of_iter, num_of_found_isomorphisms

def ullman2(unused_colums, current_row, G : np.array, P : np.array, M : np.array, M0 : np.array):
    global iteration, number_of_isomorphisms
    iteration += 1
    if current_row == M.shape[0]:
        if isomorphism(M, P, G):
            number_of_isomorphisms += 1
            return
        else:
            return
    is_worth = puring(M, P, G)
    print(M)
    print(is_worth)

    for c in unused_colums:
        if M0[current_row, c] == 1 and is_worth:
            unused_colums.remove(c)
            M[current_row, c] = 1
            ullman2(unused_colums, current_row + 1, G, P, M, M0)
            M[current_row, c] = 0
            unused_colums.append(c)
            unused_colums.sort()
    return iteration, number_of_isomorphisms

def ullman_iter2(unused_colums, current_row, G : np.array, P : np.array, M : np.array, M0 : np.array):
    num_of_iter = 0
    num_of_found_isomorphisms = 0
    X, Y = M.shape
    for i in range(Y):
        for j in range(Y):
            for k in range(Y):
                if i != j != k != i and M0[0, i] == M0[1, j] == M0[2, k] == 1:
                    M = np.zeros((X, Y))
                    M[0, i] = 1
                    M[1, j] = 1
                    M[2, k] = 1
                    if puring(M, P, G):
                        if isomorphism(M, P, G):
                            num_of_found_isomorphisms += 1
                        num_of_iter += 1
    return num_of_iter, num_of_found_isomorphisms


def main():
    global iteration, number_of_isomorphisms
    number_of_isomorphisms = 0
    iteration = -1
    m1 = Matrix()
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    for v1, v2, edge in graph_G:
        m1.insertEdge(Vertex(v1), Vertex(v2), edge)
    m2 = Matrix()
    for v1, v2, edge in graph_P:
        m2.insertEdge(Vertex(v1), Vertex(v2), edge)
    unused_colums = [i for i in range(len(m1.Matrix))]
    M = np.zeros((len(m2.Matrix), len(m1.Matrix)))
    G = np.array(m1.Matrix)
    P = np.array(m2.Matrix)
    print(G)
    print(P)
    ullman(unused_colums, 0, G, P, M)
    print("Rozwiązania rekurencyjne:")
    print("wersja 1.0")
    print("Ilość izomorfizmów: ",number_of_isomorphisms)
    print("Ilość iteracji: ",iteration)
    number_of_isomorphisms = 0
    iteration = -1
    M0 = np.zeros(M.shape)
    for x in range(M.shape[0]):#3
        for y in range(M.shape[1]):#6
            if sum(P[x]) <= sum(G[y]):
                M0[x][y] = 1
    ullman1(unused_colums, 0, G, P, M, M0)
    print("wersja 2.0")
    print("Ilość izomorfizmów: ",number_of_isomorphisms)
    print("Ilość iteracji: ",iteration)
    number_of_isomorphisms = 0
    iteration = -1
    ullman2(unused_colums, 0, G, P, M, M0)
    print("wersja 3.0")
    print("Ilość izomorfizmów: ",number_of_isomorphisms)
    print("Ilość iteracji: ",iteration)
    print()
    print("Rozwiązania iteracyjne:")
    iterations, num_of_found_isomorphisms = ullman_iter(unused_colums, 0, G, P, M)
    print("wersja 1.0")
    print("Ilość izomorfizmów: ",num_of_found_isomorphisms)
    print("Ilość iteracji: ",iterations)
    iterations, num_of_found_isomorphisms = ullman_iter1(unused_colums, 0, G, P, M, M0)
    print("wersja 2.0")
    print("Ilość izomorfizmów: ",num_of_found_isomorphisms)
    print("Ilość iteracji: ",iterations)
    iterations, num_of_found_isomorphisms = ullman_iter2(unused_colums, 0, G, P, M, M0)
    print("wersja 3.0")
    print("Ilość izomorfizmów: ", num_of_found_isomorphisms)
    print("Ilość iteracji: ", iterations)
    print()


if __name__ == '__main__':
    main()
