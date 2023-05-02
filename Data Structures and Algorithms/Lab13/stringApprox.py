import time
import numpy as np

def stringCompareRecursion(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i 
    swaps = stringCompareRecursion(P, T, i-1, j-1) + 1 if P[i] != T[j] else 0
    insertions = stringCompareRecursion(P, T, i, j-1) + 1
    deletitions = stringCompareRecursion(P, T, i-1, j) + 1
 
    lowestCost = min(swaps, insertions, deletitions) 
    
    return lowestCost

def stringComparePD(P, T):
    X, Y = len(P), len(T)
    swaps = np.zeros((X, Y), dtype='uint8')
    insertions = np.zeros((X, Y), dtype='uint8')
    deletitions = np.zeros((X, Y), dtype='uint8')
    D = np.zeros((X, Y), dtype='uint8')
    for x in range(X):
        D[x][0] = x
    for y in range(Y):
        D[0][y] = y

    parents = np.chararray((X, Y), unicode=True)
    parents[:] = 'X'
    
    for i in range(X):
        for j in range(Y):
            swaps[i][j] = D[i-1][j-1] + (P[i]!=T[j])
            insertions[i][j] = D[i][j-1] + 1
            deletitions[i][j] = D[i-1][j] + 1

            D[i][j] = min(swaps[i][j], insertions[i][j], deletitions[i][j])
            if P[i] == T[j]:
                parents[i][j] = 'M'
            elif D[i][j] == swaps[i][j]:
                parents[i][j] = 'S'
            elif D[i][j] == insertions[i][j]:
                parents[i][j] = 'I'
            elif D[i][j] == deletitions[i][j]:
                parents[i][j] = 'D'

    parents[0][0] = 'X'
    for x in range(1, X):
        parents[x][0] = 'D'
    for y in range(1, Y):
        parents[0][y] = 'I'

    path = []
    i, j = X-1, Y-1
    while True:
        s = parents[i][j]
        if parents[i][j] == 'X':
            break
        path.append(parents[i][j])
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            j -= 1
            i -= 1
        elif parents[i][j] == 'I':
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1

    return D[X-1][Y-1], path[::-1]

def sequenceMatch(P, T):
    X, Y = len(P), len(T)
    swaps = np.zeros((X, Y), dtype='uint8')
    insertions = np.zeros((X, Y), dtype='uint8')
    deletitions = np.zeros((X, Y), dtype='uint8')
    D = np.zeros((X, Y), dtype='uint8')
    for x in range(X):
        D[x][0] = x

    parents = np.chararray((X, Y), unicode=True)
    parents[:] = 'X'
    
    for i in range(X):
        for j in range(Y):
            swaps[i][j] = D[i-1][j-1] + (P[i]!=T[j])
            insertions[i][j] = D[i][j-1] + 1
            deletitions[i][j] = D[i-1][j] + 1

            D[i][j] = min(swaps[i][j], insertions[i][j], deletitions[i][j])
            if P[i] == T[j]:
                parents[i][j] = 'M'
            elif D[i][j] == swaps[i][j]:
                parents[i][j] = 'S'
            elif D[i][j] == insertions[i][j]:
                parents[i][j] = 'I'
            elif D[i][j] == deletitions[i][j]:
                parents[i][j] = 'D'

    parents[0][0] = 'X'
    for x in range(1, X):
        parents[x][0] = 'D'
    for y in range(1, Y):
        parents[0][y] = 'X'
    
    idx = 1
    for i in range(1, Y):
        if D[len(D)-1][i] <= D[len(D)-1][idx]:
            idx = i

    return idx - (len(P) - 1) + 1

def longestCommonSequence(P, T):
    X, Y = len(P), len(T)
    swaps = np.zeros((X, Y), dtype='uint8')
    insertions = np.zeros((X, Y), dtype='uint8')
    deletitions = np.zeros((X, Y), dtype='uint8')
    D = np.zeros((X, Y), dtype='uint8')
    for x in range(X):
        D[x][0] = x
    for y in range(Y):
        D[0][y] = y

    parents = np.chararray((X, Y), unicode=True)
    parents[:] = 'X'
    
    for i in range(1, X):
        for j in range(1, Y):
            swaps[i][j] = D[i-1][j-1] + (P[i]!=T[j]) * 100
            insertions[i][j] = D[i][j-1] + 1
            deletitions[i][j] = D[i-1][j] + 1

            D[i][j] = min(swaps[i][j], insertions[i][j], deletitions[i][j])
            if P[i] == T[j]:
                parents[i][j] = 'M'
            elif D[i][j] == insertions[i][j]:
                parents[i][j] = 'I'
            elif D[i][j] == deletitions[i][j]:
                parents[i][j] = 'D'

    parents[0][0] = 'X'
    for x in range(1, X):
        parents[x][0] = 'D'
    for y in range(1, Y):
        parents[0][y] = 'I'

    sequence = []
    i, j = X-1, Y-1
    while True:
        if parents[i][j] == 'X':
            break
        if parents[i][j] == 'M':
            sequence.append(P[i])
            j -= 1
            i -= 1
        elif parents[i][j] == 'I':
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
    return sequence[::-1]

def main():
    P = ' kot'
    T = ' kon'
    start = time.perf_counter()
    cost = stringCompareRecursion(P, T, 3, 3)
    stop = time.perf_counter()
    print(cost)
    # print("Czas obliczeń przykładu 1:", "{:.7f}".format(stop - start))


    P = ' kot'
    T = ' pies'
    start = time.perf_counter()
    cost = stringCompareRecursion(P, T, 3, 4)
    stop = time.perf_counter()
    print(cost)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))

    P = ' autobus'
    T = ' autokar'
    start = time.perf_counter()
    cost = stringCompareRecursion(P, T, len(P) - 1, len(T) - 1)
    stop = time.perf_counter()
    print(cost)
    # print("Czas obliczeń przykładu 3:", "{:.7f}".format(stop - start))

    # # PD
    # print('\nPD')

    P = ' biały autobus'
    T = ' czarny autokar'
    start = time.perf_counter()
    cost, path = stringComparePD(P, T)
    stop = time.perf_counter()
    print(cost)
    # print("Czas obliczeń przykładu 1:", "{:.7f}".format(stop - start))


    P = ' kot'
    T = ' pies'
    start = time.perf_counter()
    cost, path = stringComparePD(P, T)
    stop = time.perf_counter()
    print(cost)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))

    P = ' thou shalt not'
    T = ' you should not'
    start = time.perf_counter()
    cost, path = stringComparePD(P, T)
    stop = time.perf_counter()
    print(path)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))

    P = ' ban'
    T = ' mokeyssbanana'
    start = time.perf_counter()
    idx = sequenceMatch(P, T)
    stop = time.perf_counter()
    print(idx)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))

    P = ' bin'
    T = ' mokeyssbanana'
    start = time.perf_counter()
    seq = sequenceMatch(P, T)
    stop = time.perf_counter()
    print(seq)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))
    P = ' democrat'
    T = ' republican'
    start = time.perf_counter()
    seq = longestCommonSequence(P, T)
    stop = time.perf_counter()
    print(seq)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))

    T = ' 243517698'
    start = time.perf_counter()
    seq = longestCommonSequence(sorted(T), T)
    stop = time.perf_counter()
    print(seq)
    # print("Czas obliczeń przykładu 2:", "{:.7f}".format(stop - start))




if __name__ == '__main__':
    main()

