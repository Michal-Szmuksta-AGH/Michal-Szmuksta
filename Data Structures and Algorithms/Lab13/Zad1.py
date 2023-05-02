# SKOŃCZONE
import time
import numpy as np


def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    swaps = string_compare(P, T, i - 1, j - 1) + int(P[i] != T[j])
    inserts = string_compare(P, T, i, j - 1) + 1
    deletions = string_compare(P, T, i - 1, j) + 1

    smallest_cost = min(swaps, inserts, deletions)

    return smallest_cost


def string_compare_PD_version(P, T):
    D = np.zeros((len(P), len(T)))
    D[0, :] = [i for i in range(len(T))]
    D[:, 0] = [i for i in range(len(P))]

    Parents = np.full((len(P), len(T)), 'X')
    Parents[0, 1:] = ['I' for i in range(len(T) - 1)]
    Parents[1:, 0] = ['D' for i in range(len(P) - 1)]

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletions = D[i - 1][j] + 1

            smallest_cost = min(swaps, inserts, deletions)

            D[i][j] = smallest_cost

            if smallest_cost == swaps:
                if P[i] == T[j]:
                    Parents[i][j] = 'M'
                else:
                    Parents[i][j] = 'S'
            elif smallest_cost == inserts:
                Parents[i][j] = 'I'
            elif smallest_cost == deletions:
                Parents[i][j] = 'D'

    Parents[0][0] = 'X'
    return int(D[-1][-1]), Parents


def path_reproduction(Parent):
    i, j = Parent.shape[0] - 1, Parent.shape[1] - 1
    path = ''
    common = []
    while Parent[i][j] != 'X':
        path += Parent[i][j]
        if Parent[i][j] == 'M' or Parent[i][j] == 'S':
            i -= 1
            j -= 1
            common.append(i)
        elif Parent[i][j] == 'I':
            j -= 1
        elif Parent[i][j] == 'D':
            i -= 1
    return path[::-1], common[::-1]


def matching_substrings(P, T):
    D = np.zeros((len(P), len(T)))
    D[:, 0] = [i for i in range(len(P))]

    Parents = np.full((len(P), len(T)), 'X')
    Parents[1:, 0] = ['D' for i in range(len(P) - 1)]

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletions = D[i - 1][j] + 1

            smallest_cost = min(swaps, inserts, deletions)

            D[i][j] = smallest_cost

            if smallest_cost == swaps:
                if P[i] == T[j]:
                    Parents[i][j] = 'M'
                else:
                    Parents[i][j] = 'S'
            elif smallest_cost == inserts:
                Parents[i][j] = 'I'
            elif smallest_cost == deletions:
                Parents[i][j] = 'D'

    def goal_cell(P, T, D):
        i = len(P) - 1
        j = 0
        for k in range(1, len(T)):
            if D[i][k] < D[i][j]:
                j = k
        return j

    Parents[0][0] = 'X'
    j = goal_cell(P, T, D)
    return j - len(P) + 2, Parents


def longest_common_sequence(P, T):
    D = np.zeros((len(P), len(T)))
    D[0, :] = [i for i in range(len(T))]
    D[:, 0] = [i for i in range(len(P))]

    Parents = np.full((len(P), len(T)), 'X')
    Parents[0, 1:] = ['I' for i in range(len(T) - 1)]
    Parents[1:, 0] = ['D' for i in range(len(P) - 1)]

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                swaps = D[i - 1][j - 1] + float('inf')
            else:
                swaps = D[i - 1][j - 1]
            inserts = D[i][j - 1] + 1
            deletions = D[i - 1][j] + 1

            smallest_cost = min(swaps, inserts, deletions)

            D[i][j] = smallest_cost

            if smallest_cost == swaps:
                if P[i] == T[j]:
                    Parents[i][j] = 'M'
                else:
                    Parents[i][j] = 'S'
            elif smallest_cost == inserts:
                Parents[i][j] = 'I'
            elif smallest_cost == deletions:
                Parents[i][j] = 'D'

    Parents[0][0] = 'X'
    path, common = path_reproduction(Parents)

    sequence = ''
    for idx in range(len(P)):
        if idx - 1 in common:
            sequence += P[idx]
    return sequence


def main():
    # a)
    # t_start = time.perf_counter()
    print(string_compare(' kot', ' pies', 3, 4))
    # t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # b)
    # t_start = time.perf_counter()
    # print(string_compare_PD_version(' kot', ' pies')[0])
    # t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(string_compare_PD_version(' biały autobus', ' czarny autokar')[0])

    # c)
    print(path_reproduction(string_compare_PD_version(' thou shalt not', ' you should not')[1])[0])

    # d)
    print(matching_substrings(' ban', ' mokeyssbanana')[0])
    print(matching_substrings(' bin', ' mokeyssbanana')[0])

    # e)
    print(longest_common_sequence(' democrat', ' republican'))

    # f)
    print(longest_common_sequence(' ' + ''.join(sorted('243517698')), ' 243517698'))


if __name__ == '__main__':
    main()
