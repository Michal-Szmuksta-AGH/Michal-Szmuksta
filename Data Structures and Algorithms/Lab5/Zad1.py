class Node:
    def __init__(self, key, value, left_children=None, right_children=None):
        self.key = key
        self.value = value
        self.left_children = left_children
        self.right_children = right_children

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)

    def __repr__(self):
        return '{}: {}'.format(self.key, self.value)


class BinaryTree:
    def __init__(self):
        self.head = None

    def search(self, key):
        def _search(key, node):
            if node is None:
                return None
            elif key > node.key:
                return _search(key, node.right_children)
            elif key < node.key:
                return _search(key, node.left_children)
            elif key == node.key:
                return node.value
            else:
                raise Exception

        return _search(key, self.head)

    def insert(self, key, value):
        def _insert(node, key, value):
            if node is None:
                return Node(key, value)
            elif key < node.key:
                node.left_children = _insert(node.left_children, key, value)
                ###########
                return node
            elif key > node.key:
                node.right_children = _insert(node.right_children, key, value)
                ###########
                return node
            elif key == node.key:
                node.value = value
            else:
                raise Exception
            return node

        if self.head is None:
            self.head = Node(key, value)
        else:
            return _insert(self.head, key, value)

    def find_min_node(self, father, node):
        if node.left_children is None:
            return father, node
        elif node.left_children is not None:
            return self.find_min_node(node, node.left_children)
        else:
            raise Exception

    def delete(self, key):
        def _delete(father, node, key):
            if node is None:
                raise Exception('Brak elementu o podanym kluczu')
            elif node.key == key:
                if node.left_children is not None and node.right_children is not None:
                    if father.right_children == node:
                        temp = node.left_children
                        min_node_father, min_node = self.find_min_node(node, node.right_children)
                        if min_node_father.left_children == min_node:
                            min_node_father.left_children = min_node.right_children
                        else:
                            min_node_father.right_children = min_node.right_children
                        if node != min_node_father:
                            min_node.left_children = min_node_father
                        min_node.left_children = temp
                        father.right_children = min_node
                    elif father.left_children == node:
                        temp = node.left_children
                        min_node_father, min_node = self.find_min_node(node, node.right_children)
                        if min_node_father.left_children == min_node:
                            min_node_father.left_children = min_node.right_children
                        else:
                            min_node_father.right_children = min_node.right_children
                        if node != min_node_father:
                            min_node.right_children = min_node_father
                        min_node.left_children = temp
                        father.left_children = min_node
                elif node.left_children is not None and node.right_children is None:
                    if father.right_children == node:
                        father.right_children = node.left_children
                    elif father.left_children == node:
                        father.left_children = node.left_children
                elif node.left_children is None and node.right_children is not None:
                    if father.right_children == node:
                        father.right_children = node.right_children
                    elif father.left_children == node:
                        father.left_children = node.right_children
                elif node.left_children is None and node.right_children is None:
                    if father.right_children == node:
                        father.right_children = None
                    elif father.left_children == node:
                        father.left_children = None
            elif key > node.key:
                _delete(node, node.right_children, key)
            elif key < node.key:
                _delete(node, node.left_children, key)
            else:
                raise Exception

        if key > self.head.key:
            _delete(self.head, self.head.right_children, key)
        elif key < self.head.key:
            _delete(self.head, self.head.left_children, key)
        elif key == self.head.key:
            if self.head.right_children is None and self.head.left_children is None:
                self.head = None
            elif self.head.left_children is None and self.head.right_children is not None:
                self.head = self.head.right_children
            elif self.head.left_children is not None and self.head.right_children is None:
                self.head = self.head.left_children
            elif self.head.left_children is not None and self.head.right_children is not None:
                min_node_father, min_node = self.find_min_node(self.head, self.head.right_children)
                temp_r = self.head.right_children
                temp_l = self.head.left_children
                self.head = min_node
                if min_node_father.left_children == min_node:
                    min_node_father.left_children = min_node.right_children
                else:
                    min_node_father.right_children = min_node.right_children
                min_node.right_children = None
                self.head.right_children = temp_r
                self.head.left_children = temp_l
            else:
                raise Exception
        else:
            raise Exception


    def print(self):
        lst = []

        def _print(node):
            if node.left_children is not None and node.right_children is not None:
                _print(node.left_children)
                lst.append(node)
                _print(node.right_children)
            elif node.left_children is not None and node.right_children is None:
                _print(node.left_children)
                lst.append(node)
            elif node.left_children is None and node.right_children is not None:
                lst.append(node)
                _print(node.right_children)
            elif node.left_children is None and node.right_children is None:
                lst.append(node)
            else:
                raise Exception

        if self.head is None:
            print(lst)
        else:
            _print(self.head)
            print(lst)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left_children)
            right_height = self.height(node.right_children)
            return max(left_height, right_height) + 1

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right_children, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left_children, lvl + 5)


def main():
    X = BinaryTree()
    for k, v in {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K',
                 24: 'L'}.items():
        X.insert(k, v)
    X.print_tree()
    X.print()
    print(X.search(24))
    X.insert(20, 'AA')
    X.insert(6, 'M')
    X.delete(62)
    X.insert(59, 'N')
    X.insert(100, 'P')
    X.delete(8)
    X.delete(15)
    X.insert(55, 'R')
    X.delete(50)
    X.delete(5)
    X.delete(24)
    print(X.height(X.head))
    X.print()
    X.print_tree()


if __name__ == '__main__':
    main()
