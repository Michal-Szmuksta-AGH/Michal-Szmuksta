# NIESKOŃCZONE

class Elem:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return str(self.data)


class MyTab:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        string = '{'
        for el in self.tab:
            if el is None or el == -1:
                pass
            else:
                string += str(el.key) + ': ' + str(el.data) + ', '
        if len(string) <= 2:
            string = '{}'
        else:
            string = string[:-2] + '}'
        return string

    def print_tab(self):
        string = '['
        for el in self.tab:
            string += str(el) + ', '
        string = string[:-2] + ']'
        print(string)

    def hash(self, key):
        if isinstance(key, str):
            s = 0
            for i in key:
                s += ord(i)
            key_k = s
        elif isinstance(key, int) or isinstance(key, float):
            key_k = key
        else:
            raise ValueError
        key_i = key_k % len(self.tab)
        return key_i

    def is_in_conflict(self, key_i, key_k, flag='d'):
        if self.tab[key_i] is None or (self.tab[key_i] == -1 and flag == 'd'):
            return False
        elif self.tab[key_i] == -1 and flag != 'd':
            return True
        elif self.tab[self.hash(key_i)].key != key_k:
            return True
        else:
            return False

    def conflict(self, key_i, key_k, i=1, flag='d'):
        if not self.is_in_conflict(key_i, key_k, flag):
            return key_i
        elif i == len(self.tab):
            raise OverflowError
        else:
            return self.conflict((self.hash(key_k) + self.c1 * i + self.c2 * i ** 2) % len(self.tab), key_k, i + 1,
                                 flag)

    def insert(self, key_k, data):
        key_i = self.hash(key_k)
        try:
            if not self.is_in_conflict(key_i, key_k):
                self.tab[key_i] = Elem(key_k, data)
            else:
                key_i = self.conflict(self.hash(key_i), key_k)
                self.tab[key_i] = Elem(key_k, data)
        except OverflowError:
            print('Brak miejsca')

    def search(self, key_k):
        key_i = self.hash(key_k)
        try:
            if not self.is_in_conflict(key_i, key_k, 's'):
                return self.tab[key_i].data
            else:
                key_i = self.conflict(self.hash(key_i), key_k, 1, 's')
                return self.tab[key_i].data
        except OverflowError:
            return None

    def remove(self, key_k):
        key_i = self.hash(key_k)
        try:
            if not self.is_in_conflict(key_i, key_k):
                self.tab[key_i] = -1
            else:
                key_i = self.conflict(self.hash(key_i), key_k)
                self.tab[key_i] = -1
        except OverflowError:
            print('Brak klucza')


def main():
    def test_1(size, c1, c2):
        tab1 = MyTab(size, c1, c2)
        for i, l in zip([1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15],
                        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']):
            tab1.insert(i, l)
        print(tab1)
        print(tab1.search(5))
        print(tab1.search(14))
        tab1.insert(5, 'Ala')
        print(tab1.search(5))
        tab1.remove(5)
        print(tab1)
        print(tab1.search(31))
        tab1.insert('W', 'test')
        print(tab1)

    def test_2(size, c1, c2):
        tab2 = MyTab(size, c1, c2)
        for i, l in zip(range(size), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']):
            tab2.insert(13 * (i + 1), l)
        print(tab2)

    test_1(13, 1, 0)
    test_2(13, 1, 0)
    test_2(13, 0, 1)
    test_1(13, 0, 1)


if __name__ == '__main__':
    main()
