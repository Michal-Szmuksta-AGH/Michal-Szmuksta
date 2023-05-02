from random import random
from string import ascii_uppercase
class Element:
    def __init__(self, maxLevel, value=None, key=None):
        self.value = value
        self.key = key
        self.maxLevel = maxLevel
        self.next = [None for i in range(maxLevel)]

    def __str__(self):
        return '{' + f'{self.key}:{self.value}' + '}'

class SkipList:
    def __init__(self, maxLevel):
        self.head = Element(maxLevel)

    def findPreviusOnEachLevel(self, key):
        prevLst = [None for i in range(self.head.maxLevel)]
        element = self.head
        for i in reversed(range(self.head.maxLevel)):
            while element.next[i] is not None and element.next[i].key < key:
                element = element.next[i]
            prevLst[i] = element
        return prevLst

    def search(self, key):
        prevLst = self.findPreviusOnEachLevel(key)
        if prevLst is not None:
            if prevLst[0].next[0] is not None and prevLst[0].next[0].key == key:
                return prevLst[0].next[0]
        return None

    def insert(self, value, key):
        prevLst = self.findPreviusOnEachLevel(key)
        if self.search(key) is None:
            new_element = Element(self.randomLevel(), value, key)
            for i in range(new_element.maxLevel):
                new_element.next[i] = prevLst[i].next[i]
                prevLst[i].next[i] = new_element
        else:
            self.search(key).value = value

    def remove(self, key):
        toRemove = self.search(key)
        if toRemove is not None:
            prevLst = self.findPreviusOnEachLevel(key)
            for prev in prevLst:
                for i in range(min(toRemove.maxLevel, prev.maxLevel)):
                    if prev.next[i] == toRemove:
                        prev.next[i] = toRemove.next[i]
            return toRemove.value
        else:
            return None

    def randomLevel(self):
        lvl = 1
        while random() < 0.5 and lvl < self.head.maxLevel:
            lvl += 1
        return lvl

    def displayList_(self):
        node = self.head.next[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.head.maxLevel-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while(node != None):
                while node.key>keys[idx]:
                    print("  ", end=" ")
                    idx+=1
                idx+=1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

    def __str__(self):
        s = ''
        element = self.head.next[0]
        while element is not None:
            s += str(element)
            if element.next[0] is not None:
                s += ' -> '
            element = element.next[0]
        return s

def main():
    skiplst = SkipList(4)
    for i in range(1, 16):
        skiplst.insert(ascii_uppercase[i - 1], i)
    print(skiplst)
    skiplst.displayList_()
    print(skiplst.search(2).value)
    skiplst.insert('Z', 2)
    print(skiplst.search(2).value)
    skiplst.remove(5)
    skiplst.remove(6)
    skiplst.remove(7)
    print(skiplst)
    skiplst.displayList_()
    skiplst.insert('W', 6)
    print(skiplst)
    skiplst.displayList_()

    print('---ODWROTNIE---')
    skipLstReversed = SkipList(4)
    for i in reversed(range(1, 16)):
        skiplst.insert(ascii_uppercase[-i + 15], i)
    print(skiplst)
    skiplst.displayList_()
    print(skiplst.search(2).value)
    skiplst.insert('Z', 2)
    print(skiplst.search(2).value)
    skiplst.remove(5)
    skiplst.remove(6)
    skiplst.remove(7)
    print(skiplst)
    skiplst.displayList_()
    skiplst.insert('W', 6)
    print(skiplst)
    skiplst.displayList_()

main()