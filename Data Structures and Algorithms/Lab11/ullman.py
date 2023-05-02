import numpy as np
from copy import copy


class Vertex:
    def __init__(self, value) -> None:
        self.value = value

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __str__(self):
        return f'{self.value}'


class Edge:
    def __init__(self, v1, v2) -> None:
        self.startVertex = v1
        self.endVertex = v2


class GraphMat:
    def __init__(self) -> None:
        self.adjacencyMatrix = []
        self.helpDict = {}
        self.helpList = []

    def insertVertex(self, vertex: Vertex):
        self.helpList.append(vertex)
        self.helpDict[vertex] = len(self.helpList) - 1
        self.adjacencyMatrix.append([])
        for i in range(self.getOrder()):
            self.adjacencyMatrix[i] += [0] * (self.getOrder() - len(self.adjacencyMatrix[i]))

    def insertEdge(self, vertex1, vertex2, weight):
        vertex1, vertex2 = Vertex(vertex1), Vertex(vertex2)
        if vertex1 not in self.helpList:
            self.insertVertex(vertex1)
        if vertex2 not in self.helpList:
            self.insertVertex(vertex2)
        v1Idx, v2Idx = self.getVertexIdx(vertex1), self.getVertexIdx(vertex2)
        self.adjacencyMatrix[v1Idx][v2Idx] = weight
        self.adjacencyMatrix[v2Idx][v1Idx] = weight

    def deleteVertex(self, vertex: Vertex):
        idx = self.getVertexIdx(vertex)
        self.helpList.remove(vertex)
        self.helpDict.pop(vertex)
        for i in range(idx, len(self.helpList)):
            self.helpDict[i] = self.helpDict.pop(i + 1)
        self.adjacencyMatrix.pop(idx)
        for col in self.adjacencyMatrix:
            col.pop(idx)

    def deleteEdge(self, vertex1: Vertex, vertex2: Vertex):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        # self.adjacencyMatrix[idx1][idx2] = 0
        # self.adjacencyMatrix[idx2][idx1] = 0

    def getVertexIdx(self, vertex: Vertex):
        return self.helpDict.get(vertex)

    def getVertex(self, id) -> Vertex:
        return self.helpList[id]

    def getOrder(self):
        return len(self.adjacencyMatrix)

    def size(self):
        size = sum([sum(self.adjacencyMatrix[i]) for i in range(self.order())])
        return size // 2

    def edges(self):
        edgesList = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.adjacencyMatrix[i][j] == 1:
                    edgesList.append((self.getVertex(i).value, self.getVertex(j).value))
        return edgesList

    def neighbours(self, vertxID):
        n = []
        for vertex, edge in enumerate(self.adjacencyMatrix[vertxID]):
            if edge != 0:
                n.append(self.getVertex(vertex))
        return n


def dfs(graph, s: int = 0):
    stack = [s]
    visited = []
    while len(stack) > 0:
        u = stack.pop()
        if u not in visited:
            visited.append(u)
            for v in graph.fromVertexEdges(u):
                stack.append(v)
    return visited


def bfs(graph, s: int = 0):
    stack = [s]
    visited = []
    while len(stack) > 0:
        u = stack.pop(0)
        if u not in visited:
            visited.append(u)
            for v in reversed(graph.fromVertexEdges(u)):
                stack.append(v)
    return visited


def printGraph(g):
    n = g.getOrder()
    print("------GRAPH------", n)
    for i in range(n - 1):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.fromVertexEdges(i)
        for v in nbrs:
            print(v.value, end=";")
        print()
    print("-------------------")


def ullmanV1(usedColumns, currentRow, G, P, M=None, recursionCounter=0, solutions=0):
    if usedColumns is None:
        usedColumns = []
    if M is None:
        M = np.zeros((len(P), len(G)), dtype='uint8')
    if currentRow == M.shape[0]:
        if np.array_equal(P, M @ (M @ G).T):
            return solutions + 1, recursionCounter
        else:
            return solutions, recursionCounter
    newM = copy(M)
    for c in range(M.shape[1]):
        if c not in usedColumns:
            for i in range(M.shape[1]):
                newM[currentRow][i] = 0
            newM[currentRow][c] = 1
            usedColumns.append(c)
            solutions, recursionCounter = ullmanV1(usedColumns, currentRow + 1, G, P, newM, recursionCounter, solutions)
            recursionCounter += 1
            usedColumns.pop()
    return solutions, recursionCounter


def ullmanV2(usedColumns, currentRow, G, P, M0, M=None, recursionCounter=0, solutions=0):
    if usedColumns is None:
        usedColumns = []
    if M is None:
        M = np.zeros((len(P), len(G)), dtype='uint8')
    if currentRow == M.shape[0]:
        if np.array_equal(P, M @ (M @ G).T):
            return solutions + 1, recursionCounter
        else:
            return solutions, recursionCounter
    newM = copy(M)
    for c in range(M.shape[1]):
        if c not in usedColumns and M0[currentRow][c] == 1:
            for i in range(M.shape[1]):
                newM[currentRow][i] = 0
            newM[currentRow][c] = 1
            usedColumns.append(c)
            solutions, recursionCounter = ullmanV2(usedColumns, currentRow + 1, G, P, M0, newM, recursionCounter,
                                                   solutions)
            recursionCounter += 1
            usedColumns.pop()
    return solutions, recursionCounter


def ullmanV3(usedColumns, currentRow, G, P, M0, M=None, recursionCounter=0, solutions=0):
    if usedColumns is None:
        usedColumns = []
    if M is None:
        M = np.zeros((len(P), len(G)), dtype='int')
    if currentRow == M.shape[0]:
        if np.array_equal(P, M @ (M @ G).T):
            return solutions + 1, recursionCounter
        else:
            return solutions, recursionCounter

    newM = copy(M)
    if currentRow == M.shape[0] - 1:
        prune(newM, G, P)
    if currentRow >= 1:
        for row in newM[:currentRow]:
            if row.sum() == 0:
                return solutions, recursionCounter
    for c in range(M.shape[1]):
        if c not in usedColumns and M0[currentRow][c] == 1:
            for i in range(M.shape[1]):
                newM[currentRow][i] = 0
            newM[currentRow][c] = 1
            usedColumns.append(c)
            solutions, recursionCounter = ullmanV3(usedColumns, currentRow + 1, G, P, M0, newM, recursionCounter,
                                                   solutions)
            recursionCounter += 1
            usedColumns.pop()
    return solutions, recursionCounter


def prune(M, G, P):
    idxs = []
    # all (i, j) where M is 1
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i][j] == 1:
                idxs.append((i, j))
    # do
    changed = True
    while changed:
        changed = False
        # for all (i, j) where M is 1
        for i, j in idxs:
            # all neighbours x of vi in P
            neighboursVi = []
            for k in range(len(P[i])):
                if P[i][k] == 1:
                    neighboursVi.append(k)
            # neighbours y of vj in G
            neighboursVj = []
            for k in range(len(G[j])):
                if G[j][k] == 1:
                    neighboursVj.append(k)
            # for all neigbours x of vi in P
            exist = False
            for x in neighboursVi:
                for y in neighboursVj:
                    if M[x][y] == 1:
                        exist = True
            if exist is False:
                changed = True
                M[i][j] = 0
                idxs.pop(idxs.index((i, j)))


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    G = GraphMat()
    P = GraphMat()

    for v1, v2, w in graph_G:
        G.insertEdge(v1, v2, w)

    for v1, v2, w in graph_P:
        P.insertEdge(v1, v2, w)

    print(ullmanV1(None, 0, np.array(G.adjacencyMatrix), np.array(P.adjacencyMatrix)))

    M0 = np.zeros((P.getOrder(), G.getOrder()), dtype='uint8')
    for i in range(M0.shape[0]):
        for j in range(M0.shape[1]):
            if len(P.neighbours(i)) <= len(G.neighbours(j)):
                M0[i][j] = 1

    print(ullmanV2(None, 0, np.array(G.adjacencyMatrix), np.array(P.adjacencyMatrix), M0))
    # print(np.array(P.adjacencyMatrix))
    # print(np.array(P.adjacencyMatrix)[0])
    print(ullmanV3(None, 0, np.array(G.adjacencyMatrix), np.array(P.adjacencyMatrix), M0))


if __name__ == '__main__':
    main()
