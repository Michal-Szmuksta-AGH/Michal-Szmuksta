class Vertex:
    def __init__(self, value) -> None:
        self.value = value

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


class Edge:
    def __init__(self, s: Vertex, t: Vertex, capacity: int, isResidual: bool) -> None:
        self.s = s
        self.t = t
        self.capacity = capacity
        self.isResidual = isResidual
        self.residual = capacity
        self.flow = 0

    def __str__(self):
        return f'{self.capacity} {self.flow} {self.residual} {self.isResidual}'

    def __repr__(self):
        return f'{self.capacity} {self.flow} {self.residual} {self.isResidual}'


class Graph:
    def __init__(self) -> None:
        self.adjacencyList = []
        self.helpDict = {}
        self.helpList = []

    def insertVertex(self, vertex: Vertex):
        self.helpList.append(vertex)
        self.helpDict[vertex] = len(self.helpList) - 1
        self.adjacencyList.append([])

    def insertEdge(self, vertex1, vertex2, capacity):
        vertex1, vertex2 = Vertex(vertex1), Vertex(vertex2)
        if vertex1 not in self.helpList:
            self.insertVertex(vertex1)
        if vertex2 not in self.helpList:
            self.insertVertex(vertex2)
        edge = Edge(vertex1, vertex2, capacity, isResidual=False)
        self.adjacencyList[self.getVertexIdx(vertex1)].append(edge)
        edgeR = Edge(vertex2, vertex1, capacity=0, isResidual=True)
        self.adjacencyList[self.getVertexIdx(vertex2)].append(edgeR)

    def getVertexIdx(self, vertex: Vertex):
        return self.helpDict.get(vertex)

    def getVertex(self, id) -> Vertex:
        return self.helpList[id]

    def getOrder(self):
        return len(self.adjacencyList)

    def size(self):
        size = 0
        for vertex in self.adjacencyList:
            size += len(vertex)
        return size // 2

    def neighbours(self, vertexID):
        # edges = self.adjacencyList[vertexID]
        # neighbours = []
        # for edge in edges:
        #     neighbours.append(self.getVertexIdx(edge.t))
        return self.adjacencyList[vertexID]

    def fromToEdge(self, v1, v2):
        neighboursEdges = self.neighbours(v1)
        for edge in neighboursEdges:
            if self.getVertexIdx(edge.t) == v2:
                return edge



def printGraph(g):
    n = g.getOrder()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for edge in nbrs:
            print(edge.t, edge.capacity, edge.flow, edge.residual, edge.isResidual, end=";")
        print()
    print("-------------------")


def bfs(g: Graph, s=0):
    stack = [s]
    visited = [s]
    parent = [-1] * g.getOrder()
    while len(stack) > 0:
        u = stack.pop(0)
        neighboursEdges = g.neighbours(u)
        for edge in neighboursEdges:
            nIdx = g.getVertexIdx(edge.t)
            if not nIdx in visited and edge.residual > 0:
                stack.append(nIdx)
                visited.append(nIdx)
                parent[nIdx] = u
    return parent


def pathAnalysis(g: Graph, start, end, parent):
    idx = end
    if parent[idx] == -1:
        return -1
    minCapacity = float('inf')
    while idx != start:
        parentIdx = parent[idx]
        neighbourEdges = g.neighbours(parentIdx)
        for edge in neighbourEdges:
            if edge.isResidual is False and g.getVertexIdx(edge.t) == idx:
                if edge.residual < minCapacity:
                    minCapacity = edge.residual
                break
        idx = parentIdx
    return minCapacity


def pathAugmentation(g: Graph, start, end, parent, minCapacity):
    idx = end
    if parent[idx] == -1:
        return 0
    while idx != start:
        parentIdx = parent[idx]
        # Real parent ~> vertex edge
        neighboursEdges = g.neighbours(parentIdx)
        for edge in neighboursEdges:
            if g.getVertexIdx(edge.t) == idx and edge.isResidual is False:
                edge.flow += minCapacity
                edge.residual -= minCapacity
                break
        # Residual vertex ~> parent edge
        neighboursEdges = g.neighbours(idx)
        for edge in neighboursEdges:
            if g.getVertexIdx(edge.t) == parentIdx and edge.isResidual is True:
                edge.residual += minCapacity
                break
        idx = parentIdx


def ff(g: Graph, start, end):
    parent = bfs(g, start)
    idx = end
    while idx != start or idx == -1:
        idx = parent[idx]
    if idx == -1:
        return -1
    minCapacity = pathAnalysis(g, start, end, parent)
    totalCapacity = 0
    while minCapacity > 0:
        pathAugmentation(g, start, end, parent, minCapacity)
        parent = bfs(g, start)
        minCapacity = pathAnalysis(g, start, end, parent)
    inFlowEdges = g.neighbours(end)
    for edge in inFlowEdges:
        totalCapacity += edge.residual
    return totalCapacity


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    g = Graph()
    for v1, v2, c in graf_0:
        g.insertEdge(v1, v2, c)
    print(ff(g, 0, 2))
    printGraph(g)

    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    g = Graph()
    for v1, v2, c in graf_1:
        g.insertEdge(v1, v2, c)
    print(ff(g, 0, 4))
    printGraph(g)

    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

    g = Graph()
    for v1, v2, c in graf_2:
        g.insertEdge(v1, v2, c)
    print(ff(g, 0, 6))
    printGraph(g)

    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    g = Graph()
    for v1, v2, c in graf_3:
        g.insertEdge(v1, v2, c)
    print(ff(g, 0, 4))
    printGraph(g)


if __name__ == '__main__':
    main()