# SKOŃCZONE

import polska


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
                i.append(None)
            if len(self.matrix) == 0:
                self.matrix.append([None])
            else:
                self.matrix.append([None] * (self.dict[vertex] + 1))

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
        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None
        self.matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = None

    def getVertexIdx(self, vertex):
        return self.dict.get(vertex)

    def getVertex(self, vertex_idx):
        for k, v in self.dict.items():
            if v == vertex_idx:
                return k

    def neighbours(self, vertex_idx):
        idx_list = []
        for i, el in enumerate(self.matrix[vertex_idx]):
            if el is not None:
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
                if j is not None:
                    size += 1
            k += 1
        return size

    def edges(self):
        # Zmienić przy skierowanym
        lst = []
        k = 0
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row[k:]):
                if col is not None:
                    lst.append((self.getVertex(i).key, self.getVertex(j + k).key))
            k += 1
        return lst


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


def main():
    graph_1 = NeighborhoodMatrixGraph()
    for x, y in polska.graf:
        v1 = Vertex(x)
        v2 = Vertex(y)
        e = Edge(x + y)
        graph_1.insertVertex(v1)
        graph_1.insertVertex(v2)
        graph_1.insertEdge(v1, v2, e)
    graph_1.deleteVertex(Vertex('K'))
    graph_1.deleteEdge(Vertex('W'), Vertex('E'))

    graph_2 = NeighborhoodListGraph()
    for x, y in polska.graf:
        v1 = Vertex(x)
        v2 = Vertex(y)
        e = Edge(x + y)
        graph_2.insertVertex(v1)
        graph_2.insertVertex(v2)
        graph_2.insertEdge(v1, v2, e)
    graph_2.deleteVertex(Vertex('K'))
    graph_2.deleteEdge(Vertex('W'), Vertex('E'))

    polska.draw_map(graph_1.edges())
    polska.draw_map(graph_2.edges())


if __name__ == '__main__':
    main()
