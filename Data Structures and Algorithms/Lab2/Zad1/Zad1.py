from copy import deepcopy


class Head:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Mylist:
    def __init__(self):
        self.head = None

    @classmethod
    def create(cls):
        return cls()

    def destroy(self):
        self.head = None

    def add(self, element):
        self.head = Head(element, self.head)

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        n = self.head
        i = 0
        while n is not None:
            i = i + 1
            n = n.next
        return i

    def get(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def __str__(self):
        n = self.head
        string = '['
        while n is not None:
            string = string + str(n)
            n = n.next
            if n is not None:
                string = string + ', '
        return string + ']'

    def append(self, element):
        if self.head is None:
            self.head = Head(element)
        else:
            n = self.head
            m = self.head.next
            while m is not None:
                n = n.next
                m = m.next
            n.next = Head(element)

    def pop(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            m = self.head.next.next
            while m is not None:
                n = n.next
                m = m.next
            n.next = None

    def take(self, n):
        length = self.length()
        if n >= length:
            return deepcopy(self)
        else:
            m = self.head
            new_list = Mylist().create()
            for i in range(n):
                new_list.append(m.data)
                m = m.next
            return new_list

    def drop(self, n):
        length = self.length()
        if n > length:
            return Mylist().create()
        else:
            m = self.head
            new_list = Mylist().create()
            for i in range(n):
                m = m.next
            while m is not None:
                new_list.append(m.data)
                m = m.next
            return new_list


def main():
    universities = [('AGH', 'Kraków', 1919),
                    ('UJ', 'Kraków', 1364),
                    ('PW', 'Warszawa', 1915),
                    ('UW', 'Warszawa', 1915),
                    ('UP', 'Poznań', 1919),
                    ('PG', 'Gdańsk', 1945)]
    x = Mylist.create()
    print('Stworzenie nowej listy:')
    print(x)
    print('\nDodanie elementów do listy na początek za pomocą metody add (odwrotna kolejność):')
    for u in universities:
        x.add(u)
    print(x)
    print('\nUsunięcie dwóch pierwszych elementów z listy za pomocą metody remove:')
    for i in range(2):
        x.remove()
    print(x)
    print('\nSprawdzenie czy lista jest pusta:')
    print(x.is_empty())
    print('\nSprawdzenie długości listy:')
    print(x.length())
    print('\nPobranie pierwszego elementu listy:')
    print(x.get())
    print('\nUsunięcie stworzonej listy:')
    x.destroy()
    print(x)
    print('\nSprawdzenie czy lista jest pusta:')
    print(x.is_empty())
    print('\nDodanie do listy elementów na koniec za pomocą metody append (poprawna kolejność):')
    for u in universities:
        x.append(u)
    print(x)
    print('\nUsunięcie dwóch ostatnich elementów listy za pomocą metody pop:')
    for i in range(2):
        x.pop()
    print(x)
    print('\nStworzenie nowej listy zawierającej 2 pierwsze elementy listy wyjściowej za pomocą metody take:')
    y = x.take(2)
    print(y)
    print('\nStworzenie nowej listy zawierającej 2 ostatnie elementy listy wyjściowej za pomocą metody drop:')
    z = x.drop(2)
    print(z)
    print('\nDowód na to, że lista wyjściowa nie została zmieniona:')
    print(x)


if __name__ == "__main__":
    main()
