# NIESKOŃCZONE

class Queue:
    def __init__(self, size=5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.save_idx = 0
        self.read_idx = 0

    def __str__(self):
        string = '['
        if self.save_idx < self.read_idx:
            for i in range(self.read_idx, self.size):
                string += str(self.tab[i]) + ', '
            for i in range(self.save_idx):
                if i != self.save_idx - 1:
                    string += str(self.tab[i]) + ', '
                else:
                    string += str(self.tab[i])
        elif self.save_idx > self.read_idx:
            for i in range(self.read_idx, self.save_idx):
                if i != self.save_idx - 1:
                    string += str(self.tab[i]) + ', '
                else:
                    string += str(self.tab[i])
        else:
            pass
        return string + ']'

    def return_tab(self):
        return self.tab

    def is_empty(self):
        if self.read_idx == self.save_idx:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty() is True:
            return None
        else:
            return self.tab[self.read_idx]

    def dequeue(self):
        if self.is_empty() is True:
            return None
        elif self.read_idx + 1 == self.size:
            i = self.read_idx
            self.read_idx = 0
            return self.tab[i]
        else:
            i = self.read_idx
            self.read_idx += 1
            return self.tab[i]

    def enqueue(self, data):
        self.tab[self.save_idx] = data
        if self.save_idx + 1 == self.size:
            self.save_idx = 0
        else:
            self.save_idx += 1
        if self.save_idx == self.read_idx:
            self.tab = realloc(self.tab, 2 * self.size)
            i = self.save_idx
            for i in range(self.size - self.save_idx):
                self.tab[-i - 1] = self.tab[self.size - i - 1]
            self.read_idx = self.read_idx + self.size
            self.size = self.size * 2


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


def main():
    Q = Queue(5)
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')
    for i in range(1, 5):
        Q.enqueue(i)
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')
    print('Odczyt:', Q.dequeue(), '\n')
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')
    print('Odczyt:', Q.peek(), '\n')
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')
    for i in range(5, 9):
        Q.enqueue(i)
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')
    for i in range(1, 9):
        print('Odczyt:', Q.dequeue(), '\n')
    print('Tablica:', Q.return_tab())
    print('Kolejka:', Q, '\n')


if __name__ == '__main__':
    main()
