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
        return sorted(idx_list)

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
        return sorted(lst)

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


# def bfs(graph, vertex_idx=0, visited=None):
#     if visited is None:
#         visited = []
#     visited.append(vertex_idx)
#     for i in graph.neighbours(vertex_idx):
#         if i not in visited:
#             bfs(graph, i, visited)
#     return visited


def bfs(graph, vertex_idx=0):
    path = []
    queue = [vertex_idx]
    visited = [False] * graph.size()
    visited[vertex_idx] = True
    while len(queue) != 0:
        vertex = queue.pop(0)
        path.append(vertex)
        for neighbour_idx in graph.neighbours(vertex):
            if visited[neighbour_idx] is True:
                pass
            else:
                queue.append(neighbour_idx)
                visited[neighbour_idx] = True
    return path


def dfs(graph, vertex_idx=0):
    path = []
    stack = [vertex_idx]
    visited = [False] * graph.size()
    visited[vertex_idx] = True
    while len(stack) != 0:
        vertex = stack.pop()
        path.append(vertex)
        for neighbour_idx in graph.neighbours(vertex):
            if visited[neighbour_idx] is True:
                pass
            else:
                stack.append(neighbour_idx)
                visited[neighbour_idx] = True
    return path


def color_the_graph(graph, flag):
    if flag == 'dfs':
        path = dfs(graph)
    elif flag == 'bfs':
        path = bfs(graph)
    else:
        raise Exception
    color_list = graph.order() * [-1]
    color_list[path[0]] = 0
    for vertex_idx in path[1::]:
        colors = graph.order() * [False]
        for neighbour_idx in graph.neighbours(vertex_idx):
            if color_list[neighbour_idx] > -1:
                colors[color_list[neighbour_idx]] = True
        i = 0
        while colors[i] is True:
            i += 1
        color_list[vertex_idx] = i
    return_table = []
    for idx, color in enumerate(color_list):
        return_table.append((graph.getVertex(idx).key, color))
    return return_table


def main():
    graph_1 = NeighborhoodMatrixGraph()
    for x, y in polska.graf:
        v1 = Vertex(x)
        v2 = Vertex(y)
        e = Edge(x + y)
        graph_1.insertVertex(v1)
        graph_1.insertVertex(v2)
        graph_1.insertEdge(v1, v2, e)

    graph_2 = NeighborhoodListGraph()
    for x, y in polska.graf:
        v1 = Vertex(x)
        v2 = Vertex(y)
        e = Edge(x + y)
        graph_2.insertVertex(v1)
        graph_2.insertVertex(v2)
        graph_2.insertEdge(v1, v2, e)

    polska.draw_map(graph_1.edges(), color_the_graph(graph_1, 'bfs'))
    polska.draw_map(graph_2.edges(), color_the_graph(graph_2, 'dfs'))


if __name__ == '__main__':
    main()
