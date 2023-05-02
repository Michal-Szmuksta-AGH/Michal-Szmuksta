# SKOŃCZONE
import random
import time


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


def make_elem_tab(tab):
    output_tab = []
    for p, d in tab:
        output_tab.append(Elem(d, p))
    return output_tab


def selection_sort(input_tab, flag):
    if flag == 'swap':
        for i, el in enumerate(input_tab):
            m = input_tab[i::].index(min(input_tab[i::])) + i
            input_tab[i], input_tab[m] = input_tab[m], input_tab[i]
    elif flag == 'shift':
        for i, el in enumerate(input_tab):
            element = input_tab.pop(input_tab[i::].index(min(input_tab[i::])) + i)
            input_tab.insert(i, element)
    else:
        raise ValueError


def main():
    x1 = make_elem_tab(
        [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')])

    x2 = make_elem_tab(
        [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')])

    selection_sort(x1, 'swap')
    print(x1)
    selection_sort(x2, 'shift')
    print(x2)

    random_list1 = []
    for i in range(10000):
        random_list1.append(int(random.random() * 1000))

    random_list2 = []
    for i in range(10000):
        random_list2.append(int(random.random() * 1000))

    t_start = time.perf_counter()
    selection_sort(random_list1, 'swap')
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania przez wybieranie (swap - niestabilny):", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    selection_sort(random_list2, 'shift')
    t_stop = time.perf_counter()
    print("Czas obliczeń sortowania przez wybieranie (shift - stabilny):", "{:.7f}".format(t_stop - t_start))


if __name__ == '__main__':
    main()
