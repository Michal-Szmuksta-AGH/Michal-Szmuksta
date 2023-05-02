from copy import deepcopy


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
    def __init__(self, v1: Vertex, v2: Vertex, weight: int) -> None:
        self.startVertex = v1
        self.endVertex = v2
        self.weight = weight

    def __str__(self):
        return f'{self.startVertex} -> {self.endVertex} : {self.weight}'


class GraphList:
    def __init__(self) -> None:
        self.adjacencyList = []
        self.helpDict = {}
        self.helpList = []

    def insertVertex(self, vertex: Vertex):
        self.helpList.append(vertex)
        self.helpDict[vertex] = len(self.helpList) - 1
        self.adjacencyList.append([])

    def insertEdge(self, vertex1, vertex2, weight):
        vertex1, vertex2 = Vertex(vertex1), Vertex(vertex2)
        if vertex1 not in self.helpList:
            self.insertVertex(vertex1)
        if vertex2 not in self.helpList:
            self.insertVertex(vertex2)
        edge = Edge(vertex1, vertex2, weight)
        self.adjacencyList[self.getVertexIdx(vertex1)].append(edge)
        edge = Edge(vertex2, vertex1, weight)
        self.adjacencyList[self.getVertexIdx(vertex2)].append(edge)

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
        return self.adjacencyList[vertexID]


def prim(g: GraphList):
    n = g.getOrder()
    intree = [0] * n
    distance = [float('inf')] * n
    parent = [-1] * n
    mst: GraphList = deepcopy(g)
    sum = 0
    for i in range(n):
        mst.adjacencyList[i] = []
    vIdx = 0

    while intree[vIdx] == 0:
        intree[vIdx] = 1
        neighbours = g.neighbours(vIdx)
        for edge in neighbours:
            nIdx = g.getVertexIdx(edge.endVertex)
            if edge.weight < distance[nIdx] and intree[nIdx] == 0:
                distance[nIdx] = edge.weight
                parent[nIdx] = vIdx

        minDist = float('inf')
        vIdx = 0
        for u in g.helpList:
            if intree[g.getVertexIdx(u)] == 0 and distance[g.getVertexIdx(u)] < minDist:
                minDist = distance[g.getVertexIdx(u)]
                vIdx = g.getVertexIdx(u)
        if minDist != float('inf'):
            sum += minDist
            vNext = g.getVertex(vIdx)
            vParent = g.getVertex(parent[vIdx])
            mst.adjacencyList[vIdx].append(Edge(vNext, vParent, minDist))
            mst.adjacencyList[parent[vIdx]].append(Edge(vParent, vNext, minDist))
    return mst, sum


def printGraph(g):
    n = g.getOrder()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for edge in nbrs:
            print(edge.endVertex, edge.weight, end=";")
        print()
    print("-------------------")


def main():
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]
    g = GraphList()
    for v1, v2, w in graf:
        g.insertEdge(v1, v2, w)

    mst, s = prim(g)
    printGraph(mst)


if __name__ == '__main__':
    main()