# SKOŃCZONE
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def are_clockwise(p, q, r):  # prawoskrętne
    a = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if a > 0:
        return True
    else:
        return False


def are_counter_clockwise(p, q, r):  # lewoskrętne
    a = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if a < 0:
        return True
    else:
        return False


def are_collinear(p, q, r):  # współliniowe
    a = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if a == 0:
        return True
    else:
        return False


def jarvis(points_table, flag):
    starting_point = Point(float('inf'), float('inf'))

    for p in points_table:
        if p.x < starting_point.x:
            starting_point = p
        elif p.x == starting_point.x and p.y < starting_point.y:
            starting_point = p

    return_list = []
    p = starting_point

    while True:
        return_list.append(p)

        if points_table.index(p) < len(points_table) - 1:
            q = points_table[points_table.index(p) + 1]
        else:
            q = points_table[points_table.index(p) - 1]

        for r in points_table:
            len_of_pr = np.sqrt((r.x - p.x) ** 2 + (r.y - p.y) ** 2)
            len_of_pq = np.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

            if flag == 'v1' and are_clockwise(p, q, r):
                q = r
            elif flag == 'v2' and (
                    are_clockwise(p, q, r) or (are_collinear(p, r, q) and len_of_pr > len_of_pq)):
                q = r

        p = q

        if p == starting_point:
            break

    return return_list


def main():
    print('Wersja 1:')
    points_table_1 = []
    for x, y in [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]:
        p = Point(x, y)
        points_table_1.append(p)
    print(jarvis(points_table_1, 'v1'))

    points_table_2 = []
    for x, y in [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]:
        p = Point(x, y)
        points_table_2.append(p)
    print(jarvis(points_table_2, 'v1'))

    print('')

    print('Wersja 2:')

    print(jarvis(points_table_1, 'v2'))

    print(jarvis(points_table_2, 'v2'))

    print('')

    points_table_3 = []
    for x, y in [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]:
        p = Point(x, y)
        points_table_3.append(p)
    print('Wersja 1:')
    print(jarvis(points_table_3, 'v1'))

    print('Wersja 2:')
    print(jarvis(points_table_3, 'v2'))


if __name__ == '__main__':
    main()
