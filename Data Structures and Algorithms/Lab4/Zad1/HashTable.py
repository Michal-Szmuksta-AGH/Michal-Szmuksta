from string import ascii_uppercase
class Pair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self):
        return '{' + f'{self.key}:{self.value}' + '}'


class HashTable:
    def __init__(self, size, c1=1, c2=0) -> None:
        self.array = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash_func(self, key):
        if isinstance(key, str):
            string, key = key, 0
            for letter in string:
                key += ord(letter)
        return key % self.size

    def solve_collision(self, hk, key):
        new_hk = hk
        for i in range(1, self.size + 1):
            if self.array[new_hk] is None or self.array[new_hk] == -1:
                return new_hk
            if self.array[new_hk].key == key:
                return new_hk
            new_hk = (hk + self.c1 * i + self.c2 * i ** 2) % self.size
        return None

    def search(self, key):
        hk = self.hash_func(key)
        new_hk = hk
        for i in range(1, self.size + 1):
            if self.array[new_hk] is None:
                return None
            elif self.array[new_hk] != -1:
                if self.array[new_hk].key == key:
                    return self.array[new_hk].value
            new_hk = (hk + self.c1 * i + self.c2 * i ** 2) % self.size

    def insert(self, value, key):
        hk = self.solve_collision(self.hash_func(key), key)
        try:
            self.array[hk] = Pair(key, value)
        except:
            return None

    def remove(self, key):
        h = self.hash_func(key)
        try:
            h = self.solve_collision(h, key)
            self.array[h] = -1
        except:
            raise Exception('Brak danej\n')

    def __str__(self) -> str:
        s = '{'
        for i, pair in enumerate(self.array):
            if not isinstance(pair, int) and pair is not None:
                s += f'{pair.key}' + ':' + f'{pair.value}'
                if i != self.size - 1:
                    s += ', '
        s += '}'
        return s


def test1(size, c1=1, c2=0):
    arr = HashTable(size, c1, c2)
    keys = [i for i in range(1, 16)]
    keys[5] = 18
    keys[6] = 31
    for i, key in enumerate(keys):
        arr.insert(ascii_uppercase[i], key)
    print(arr)
    print(arr.search(5))
    print(arr.search(14))
    arr.insert('AAAA', 5)
    print(arr.search(5))
    arr.remove(5)
    print(arr)
    print(arr.search(31))
    arr.insert('W', 'test')
    print(arr)

def test2(size, c1=1, c2=0):
    arr = HashTable(size, c1, c2)
    keys = [i * 13 for i in range(1, 16)]
    for i, key in enumerate(keys):
        arr.insert(ascii_uppercase[i], key)
    print(arr)


def main():
    test1(13)
    test2(13)
    test2(13, c1=0, c2=1)
    test1(13, c1=0, c2=1)


if __name__ == '__main__':
    main()