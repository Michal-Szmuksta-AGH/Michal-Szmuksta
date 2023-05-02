# SKOŃCZONE
import time
import random


class Elem:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return '{}: {}'.format(self.priority, self.data)

    def __repr__(self):
        return '{}: {}'.format(self.priority, self.data)

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


def right(idx):
    return 2 * idx + 2


def left(idx):
    return 2 * idx + 1


def parent(idx):
    return (idx - 1) // 2


def make_elem_tab(tab):
    output_tab = []
    for p, d in tab:
        output_tab.append(Elem(d, p))
    return output_tab


class Queue:
    def __init__(self, elements_to_sort_list=None):
        if elements_to_sort_list is None:
            self.size = 0
            self.tab = []
        else:
            self.size = len(elements_to_sort_list)
            self.tab = self.heapify(elements_to_sort_list)

    def is_empty(self):
        return True if self.size == 0 else False

    def peek(self):
        return self.tab[0] if not self.is_empty() else None

    def dequeue_in_place(self, elem_idx, tab):
        left_child = left(elem_idx)
        right_child = right(elem_idx)
        if 0 <= left_child < self.size and 0 <= right_child < self.size:
            if tab[elem_idx] < tab[left_child] <= tab[right_child]:
                tab[elem_idx], tab[right_child] = tab[right_child], tab[elem_idx]
                self.dequeue_in_place(right_child, tab)
            elif tab[elem_idx] < tab[left_child] >= tab[right_child]:
                tab[elem_idx], tab[left_child] = tab[left_child], tab[elem_idx]
                self.dequeue_in_place(left_child, tab)
            elif tab[elem_idx] < tab[right_child] <= tab[left_child]:
                tab[elem_idx], tab[left_child] = tab[left_child], tab[elem_idx]
                self.dequeue_in_place(left_child, tab)
            elif tab[elem_idx] < tab[right_child] >= tab[left_child]:
                tab[elem_idx], tab[right_child] = tab[right_child], tab[elem_idx]
                self.dequeue_in_place(right_child, tab)
        elif 0 <= left_child < self.size and (0 > right_child or right_child >= self.size):
            if tab[elem_idx] < tab[left_child]:
                tab[elem_idx], tab[left_child] = tab[left_child], tab[elem_idx]
                self.dequeue_in_place(left_child, tab)
        elif (0 > left_child or left_child >= self.size) and 0 <= right_child < self.size:
            if tab[elem_idx] < tab[right_child]:
                tab[elem_idx], tab[right_child] = tab[right_child], tab[elem_idx]
                self.dequeue_in_place(right_child, tab)
        else:
            pass

    def dequeue(self):
        if self.is_empty():
            return None
        ret = self.tab[0]
        self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
        self.size -= 1
        self.dequeue_in_place(0, self.tab)
        return ret

    def enqueue(self, data, priority):
        elem_idx = self.size
        self.tab.append(Elem(data, priority))
        self.size += 1

        def enqueue_in_place(queue, elem_idx):
            parent_idx = parent(elem_idx)
            if 0 <= parent_idx < queue.size and 0 <= elem_idx < queue.size and queue.tab[parent_idx].priority < \
                    queue.tab[elem_idx].priority:
                queue.tab[parent_idx], queue.tab[elem_idx] = queue.tab[elem_idx], queue.tab[parent_idx]
                enqueue_in_place(queue, parent_idx)

        enqueue_in_place(self, elem_idx)

    def print_tab(self, flag=None):
        if flag is None:
            size = self.size
        else:
            size = len(self.tab)
        print('{', end=' ')
        if not size == 0:
            for i in range(size - 1):
                print(self.tab[i], end=', ')
            if self.tab[size - 1]: print(self.tab[size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(left(idx), lvl + 1)

    def heapify(self, input_tab):
        idx = parent(len(input_tab) - 1)
        for i in range(idx + 1)[::-1]:
            self.dequeue_in_place(i, input_tab)
        return input_tab


def main():
    x = Queue(make_elem_tab(
        [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]))
    x.print_tab()
    x.print_tree(0, 0)
    while not x.is_empty():
        x.dequeue()
    x.print_tab('internal representation')

    random_list = []
    for i in range(10000):
        random_list.append(int(random.random() * 100))

    t_start = time.perf_counter()
    y = Queue(random_list)
    while not y.is_empty():
        y.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania przez kopcowanie (niestabilny):", "{:.7f}".format(t_stop - t_start))


if __name__ == '__main__':
    main()
