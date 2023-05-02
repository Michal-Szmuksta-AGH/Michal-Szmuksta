# SKOŃCZONE
import time


def naive(S, W):
    len_S = len(S)
    len_W = len(W)
    founded = 0
    comparisons = 0
    m = 0
    i = 0

    while m <= len_S - len_W:
        comparisons += 1
        if S[m + i] == W[i]:
            i += 1
        else:
            m += 1
            i = 0
        if i == len_W:
            founded += 1
            i = 0
            m += 1

    return founded, comparisons


def hash(W, d, q):
    len_W = len(W)
    hw = 0
    for i in range(len_W):  # N - to długość wzorca
        hw = (hw * d + ord(W[
                               i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def rabin_karp(S, W, d, q):
    len_S = len(S)
    len_W = len(W)
    hW = hash(W, d, q)

    m = 0
    founded = 0
    comparisons = 0
    while m <= len_S - len_W:
        hS = hash(S[m:m + len_W], d, q)
        comparisons += 1
        if hS == hW:
            if S[m:m + len_W] == W:
                founded += 1
        m += 1
    return founded, comparisons


def rabin_karp_rolling_hash(S, W, d, q):
    len_S = len(S)
    len_W = len(W)
    hW = hash(W, d, q)

    h = 1
    for i in range(len_W - 1):  # N - jak wyżej - długość wzorca
        h = (h * d) % q

    m = 0
    founded = 0
    comparisons = 0
    collisions = 0
    hS = hash(S[:len_W], d, q)
    while m <= len_S - len_W:
        comparisons += 1
        if hS == hW:
            if S[m:m + len_W] == W:
                founded += 1
            else:
                collisions += 1
        if m != len_S - len_W:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + len(W)])) % q
        if hS < 0:
            hS += q
        m += 1
    return founded, comparisons, collisions


def knuth_morris_pratt(S, W):
    found = 0
    comparisons = 0
    len_S = len(S)
    len_W = len(W)

    def table(W, len_W):
        pos = 1
        cnd = 0
        T = [0] * (len_W + 1)

        T[0] = -1
        while pos < len_W:
            if W[pos] == W[cnd]:
                T[pos] = T[cnd]
            else:
                T[pos] = cnd
                while cnd >= 0 and W[pos] != W[cnd]:
                    cnd = T[cnd]
            pos += 1
            cnd += 1
        T[pos] = cnd
        return T

    m = 0
    i = 0
    T = table(W, len_W)

    while m < len_S:
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len_W:
                found += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return found, comparisons


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'

    print('Metoda naiwna:')
    t_start = time.perf_counter()
    a, b = naive(S, W)
    print('{} ; {}'.format(a, b))
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('')

    print('Metoda Rabina-Karpa')
    t_start = time.perf_counter()
    a, b = rabin_karp(S, W, 256, 101)
    print('{} ; {}'.format(a, b))
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('')

    print('Metoda Rabina-Karpa w wersji rolling hash')
    t_start = time.perf_counter()
    a, b, c = rabin_karp_rolling_hash(S, W, 256, 101)
    print('{} ; {} ; {}'.format(a, b, c))
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print('')

    print('Metoda Knutha-Morrisa-Pratta (KMP)')
    t_start = time.perf_counter()
    a, b = knuth_morris_pratt(S, W)
    print('{} ; {}'.format(a, b))
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == '__main__':
    main()
