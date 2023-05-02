# NIESKOŃCZONE
from random import random


class Elem:
    def __init__(self, key, data, nr_of_levels):
        self.key = key
        self.data = data
        self.nr_of_levels = nr_of_levels
        self.next = [None for i in range(nr_of_levels)]

    def __str__(self):
        return str(self.data)


def translate_key_to_a_number(key):
    if isinstance(key, str):
        s = 0
        for i in key:
            s += ord(i)
        key_k = s
    elif isinstance(key, int) or isinstance(key, float):
        key_k = key
    else:
        raise ValueError
    return key_k


class MyTab:
    def __init__(self, max_level):
        self.head = Elem(None, None, max_level)
        self.max_level = max_level

    def random_level(self, probability=0.5):
        max_level = self.max_level
        lvl = 1
        while random() < probability and lvl < max_level:
            lvl = lvl + 1
        return lvl

    def display_list(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []  # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

    def find_path(self, key):
        max_lvl = self.max_level
        path = [None for i in range(max_lvl)]
        elem = self.head
        for i in range(max_lvl):
            while elem.next[max_lvl - i - 1] is not None and translate_key_to_a_number(
                    elem.next[max_lvl - i - 1].key) < translate_key_to_a_number(key):
                elem = elem.next[max_lvl - i - 1]
            path[max_lvl - i - 1] = elem
        return path

    def search(self, key, flag='d'):
        path = self.find_path(key)
        if path is None or len(path) == 0:
            return None
        elif path[0].next[0] is None:
            return None
        elif path[0].next[0].key == key and flag == 'd':
            return path[0].next[0].data
        elif path[0].next[0].key == key and flag != 'd':
            return path[0].next[0]
        else:
            return None

    def insert(self, key, data):
        if self.search(key, 'i') is None:
            path = self.find_path(key)
            new_elem = Elem(key, data, self.random_level())
            for i in range(new_elem.nr_of_levels):
                new_elem.next[i] = path[i].next[i]
                path[i].next[i] = new_elem
        elif self.search(key, 'i').key == key:
            self.search(key, 'i').data = data
        else:
            raise Exception

    def remove(self, key):
        if self.search(key, 'i') is None:
            raise Exception
        elif self.search(key, 'i').key == key:
            path = self.find_path(key)
            old_elem = self.search(key, 'i')
            for i in range(old_elem.nr_of_levels):
                path[i].next[i] = old_elem.next[i]
        else:
            raise Exception


def main():
    lst = MyTab(4)
    for i, l in zip(range(1, 16), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']):
        lst.insert(i, l)
    lst.display_list()
    print('')
    print(lst.search(2))
    lst.insert(2, 'Z')
    print('')
    print(lst.search(2))
    lst.remove(5)
    lst.remove(6)
    lst.remove(7)
    print('')
    lst.display_list()
    lst.insert(6, 'W')
    print('')
    lst.display_list()


if __name__ == '__main__':
    main()
