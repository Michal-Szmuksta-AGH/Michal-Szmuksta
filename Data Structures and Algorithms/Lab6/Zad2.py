# NIESKOŃCZONE

class Node:
    def __init__(self, size, keys=None, children=None):
        self.size = size
        if keys is not None:
            self.keys = keys
        else:
            self.keys = []
        if children is not None:
            self.children = children
        else:
            self.children = [None] * size


class Tree:
    def __init__(self, max_keys):
        self.max_keys = max_keys
        self.root = Node()
