# SKOŃCZONE

class Elem:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return '{}: {}'.format(self.priority, self.data)

    def __getitem__(self, item):
        pass


def right(idx):
    return 2 * idx + 2


def left(idx):
    return 2 * idx + 1


def parent(idx):
    return (idx - 1) // 2


class Queue:
    def __init__(self):
        self.tab = []

    def is_empty(self):
        return True if len(self.tab) == 0 else False

    def peek(self):
        return self.tab[0] if not self.is_empty() else None

    def dequeue(self):
        elem_idx = 0
        if self.is_empty():
            return None
        ret = self.tab[0]
        self.tab[0] = self.tab[-1]
        del self.tab[-1]

        def dequeue_in_place(queue, elem_idx):
            left_child = left(elem_idx)
            right_child = right(elem_idx)
            if 0 <= left_child < len(queue.tab) and 0 <= right_child < len(queue.tab):
                if queue.tab[elem_idx].priority < queue.tab[left_child].priority <= queue.tab[right_child].priority:
                    queue.tab[elem_idx], queue.tab[right_child] = queue.tab[right_child], queue.tab[elem_idx]
                    dequeue_in_place(queue, right_child)
                elif queue.tab[elem_idx].priority < queue.tab[left_child].priority >= queue.tab[right_child].priority:
                    queue.tab[elem_idx], queue.tab[left_child] = queue.tab[left_child], queue.tab[elem_idx]
                    dequeue_in_place(queue, left_child)
            elif 0 <= left_child < len(queue.tab) and (0 > right_child or right_child >= len(queue.tab)):
                if queue.tab[elem_idx].priority < queue.tab[left_child].priority:
                    queue.tab[elem_idx], queue.tab[left_child] = queue.tab[left_child], queue.tab[elem_idx]
                    dequeue_in_place(queue, left_child)
            elif (0 > left_child or left_child >= len(queue.tab)) and 0 <= right_child < len(queue.tab):
                if queue.tab[elem_idx].priority < queue.tab[right_child].priority:
                    queue.tab[elem_idx], queue.tab[right_child] = queue.tab[right_child], queue.tab[elem_idx]
                    dequeue_in_place(queue, right_child)

        dequeue_in_place(self, elem_idx)
        return ret

    def enqueue(self, data, priority):
        elem_idx = len(self.tab)
        self.tab.append(Elem(data, priority))

        def enqueue_in_place(queue, elem_idx):
            parent_idx = parent(elem_idx)
            if 0 <= parent_idx < len(queue.tab) and 0 <= elem_idx < len(queue.tab) and queue.tab[parent_idx].priority < \
                    queue.tab[elem_idx].priority:
                queue.tab[parent_idx], queue.tab[elem_idx] = queue.tab[elem_idx], queue.tab[parent_idx]
                enqueue_in_place(queue, parent_idx)

        enqueue_in_place(self, elem_idx)

    def print_tab(self):
        print('{', end=' ')
        if not self.is_empty():
            for i in range(len(self.tab) - 1):
                print(self.tab[i], end=', ')
            if self.tab[len(self.tab) - 1]: print(self.tab[len(self.tab) - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(left(idx), lvl + 1)


def main():
    x = Queue()
    for p, d in zip([4, 7, 6, 7, 5, 2, 2, 1], 'ALGORYTM'):
        x.enqueue(d, p)
    x.print_tree(0, 0)
    x.print_tab()
    print(x.dequeue())
    print(x.peek())
    x.print_tab()
    i = 1
    while i is not None:
        i = x.dequeue()
        print(i)
    x.print_tab()


if __name__ == '__main__':
    main()
