from typing import Union

import polska


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
        self.adjacencyMatrix = [[]]
        self.helpDict = {}
        self.helpList = []

    def insertVertex(self, vertex: Vertex):
        self.helpList.append(vertex)
        self.helpDict[vertex] = len(self.helpList) - 1
        self.adjacencyMatrix.append([])
        for i in range(self.order()):
            self.adjacencyMatrix[i] += [0] * (self.order() - len(self.adjacencyMatrix[i]))

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge):
        if vertex1 not in self.helpList:
            self.insertVertex(vertex1)
        if vertex2 not in self.helpList:
            self.insertVertex(vertex2)
        self.adjacencyMatrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = 1
        self.adjacencyMatrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = 1

    def deleteVertex(self, vertex: Vertex):
        idx = self.getVertexIdx(vertex)
        self.helpList.remove(vertex)
        self.helpDict.pop(vertex)
        for i in range(idx, len(self.helpList)):
            self.helpDict[i] = self.helpDict.pop(i+1)
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

    def order(self):
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
                n.append(vertex)
        return n

    def dfs(self, s : int = 0):
        color = 0
        stack = [(s, color)]
        visited = {}
        while len(stack) > 0:
            u, c = stack.pop()
            if self.getVertex(u) not in visited or visited[self.getVertex(u)] > c:
                visited[self.getVertex(u)] = c
                color = c + 1
                for i, v in enumerate(self.adjacencyMatrix[u]):
                    if v != 0:
                        stack.append((i, color))
        return [(k.value, c) for k, c in visited.items()]


class GraphList:
    def __init__(self) -> None:
        self.adjacencyList = []
        self.helpDict = {}
        self.helpList = []

    def insertVertex(self, vertex: Vertex):
        self.helpList.append(vertex)
        self.helpDict[vertex] = len(self.helpList) - 1
        self.adjacencyList.append([])

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge: Edge):
        if vertex1 not in self.helpList:
            self.insertVertex(vertex1)
        if vertex2 not in self.helpList:
            self.insertVertex(vertex2)
        self.adjacencyList[self.getVertexIdx(vertex1)].append(self.getVertexIdx(vertex2))
        # self.adjencyList[self.getVertexIdx(vertex2)].append(self.getVertexIdx(vertex1))

    def deleteVertex(self, vertex: Vertex):
        idx = self.getVertexIdx(vertex)
        self.helpList.remove(vertex)
        self.helpDict.pop(vertex)
        for i in range(idx, len(self.helpList)):
            self.helpDict[i] = self.helpDict.pop(i+1)
        self.adjacencyList.pop(idx)
        for edges in self.adjacencyList:
            if idx in edges: edges.remove(idx)

    def deleteEdge(self, vertex1: Vertex, vertex2: Vertex):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.adjacencyList[idx1].remove(idx2)
        self.adjacencyList[idx2].remove(idx1)

    def getVertexIdx(self, vertex: Vertex):
        return self.helpDict.get(vertex)

    def getVertex(self, id) -> Vertex:
        return self.helpList[id]

    def order(self):
        return len(self.adjacencyList)

    def size(self):
        size = 0
        for vertex in self.adjacencyList:
            size += len(vertex)
        return size // 2

    def edges(self):
        edgesList = []
        for i in range(self.order()):
            for j in self.adjacencyList[i]:
                if self.getVertex(i).value != self.getVertex(j).value:
                    edgesList.append((self.getVertex(i).value, self.getVertex(j).value))
        return edgesList

    def neighbours(self, vertexID):
        return self.adjacencyList[vertexID]

def dfs(graph, s : int = 0):
    stack = [s]
    visited = []
    while len(stack) > 0:
        u = stack.pop()
        if u not in visited:
            visited.append(u)
            for v in graph.neighbours(u):
                stack.append(v)
    return visited

def bfs(graph, s : int = 0):
    stack = [s]
    visited = []
    while len(stack) > 0:
        u = stack.pop(0)
        if u not in visited:
            visited.append(u)
            for v in reversed(graph.neighbours(u)):
                stack.append(v)
    return visited

def colorGraph(graph : Union[GraphList, GraphMat], method : str):
    if method == 'bfs':
        order = bfs(graph)
    elif method == 'dfs':
        order = dfs(graph)
    else:
        return None
    coloredGraph = {}
    for vertex in order:
        coloredGraph[vertex] = 0
    for vertex in order:
        neighbours = graph.neighbours(vertex)
        takenColors = []
        for neighbour in neighbours:
            if neighbour in coloredGraph and coloredGraph[neighbour] != 0:
                takenColors.append(coloredGraph[neighbour])
        color = 1
        while color in takenColors:
            color += 1
        coloredGraph[vertex] = color

    return [(graph.getVertex(v).value, c) for v, c in coloredGraph.items()]



def main():
    gMat = GraphMat()
    gList = GraphList()
    for edge in polska.graf:
        v1 = Vertex(edge[0])
        v2 = Vertex(edge[1])
        e = Edge(v1, v2)
        gMat.insertEdge(v1, v2, e)
        gList.insertEdge(v1, v2, e)

    # dfsPath = dfs(gMat)
    # bfsPath = bfs(gMat)
    # print('DFS path: ')
    # for vertex in dfsPath:
    #     print(gMat.getVertex(vertex).value, end=' ')
    # print()
    # print('BFS path: ')
    # for vertex in bfsPath:
    #     print(gMat.getVertex(vertex).value, end=' ')
    polska.draw_map(gMat.edges(), colorGraph(gMat, method='dfs'))


if __name__ == '__main__':
    main()