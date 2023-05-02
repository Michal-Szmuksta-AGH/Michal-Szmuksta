from copy import deepcopy


class Head:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def nil():
    return None


def cons(el, list):
    return Head(el, list)


def first(list):
    if list is None:
        return None
    else:
        return list.data


def rest(list):
    if list is None:
        return None
    else:
        return list.next


# ---------------------------------------------------------------------------------------------------------------------#


def create():
    return nil()


def destroy(list):
    return nil()


def add(element, list):
    return cons(element, list)


def remove(list):
    return rest(list)


def is_empty(list):
    if list is None:
        return True
    else:
        return False


def length(list):
    def get_length(list, i):
        if list is None:
            return 0
        else:
            return 1 + get_length(rest(list), i)
    return get_length(list, 0)


def get(list):
    return first(list)


def print_it(list):
    def get_string(list, string):
        if list is None:
            return ']'
        elif rest(list) is None:
            return str(first(list)) + ']'
        else:
            return str(first(list)) + string + str(get_string(rest(list), string))

    print('[' + get_string(list, ', '))


def append(element, list):
    if list is None:
        return cons(element, list)
    else:
        return cons(first(list), append(element, rest(list)))


def pop(list):
    if rest(list) is None:
        return None
    else:
        return cons(first(list), pop(rest(list)))


def take(n, list):
    def take_inplace(n, list, i):
        if i > n or list is None:
            return None
        else:
            return cons(first(list), take_inplace(n, rest(list), i + 1))
    return take_inplace(n, list, 1)


def drop(n, list):
    def drop_inplace(n, list, i, len):
        if list is None:
            return None
        elif len - n < i:
            return cons(first(list), drop_inplace(n, rest(list), i + 1, len))
        else:
            return drop_inplace(n, rest(list), i + 1, len)

    return drop_inplace(n, list, 1, length(list))


def main():
    universities = [('AGH', 'Kraków', 1919),
                    ('UJ', 'Kraków', 1364),
                    ('PW', 'Warszawa', 1915),
                    ('UW', 'Warszawa', 1915),
                    ('UP', 'Poznań', 1919),
                    ('PG', 'Gdańsk', 1945)]
    x = create()
    print('Stworzenie nowej listy:')
    print_it(x)
    print('\nDodanie elementów do listy na początek za pomocą funkcji add (odwrotna kolejność):')
    for u in universities:
        x = add(u, x)
    print_it(x)
    print('\nUsunięcie dwóch pierwszych elementów z listy za pomocą funkcji remove:')
    for i in range(2):
        x = remove(x)
    print_it(x)
    print('\nSprawdzenie czy lista jest pusta:')
    print(is_empty(x))
    print('\nSprawdzenie długości listy:')
    print(length(x))
    print('\nPobranie pierwszego elementu listy:')
    print(get(x))
    print('\nUsunięcie stworzonej listy:')
    x = destroy(x)
    print_it(x)
    print('\nSprawdzenie czy lista jest pusta:')
    print(is_empty(x))
    print('\nDodanie do listy elementów na koniec za pomocą funkcji append (poprawna kolejność):')
    for u in universities:
        x = append(u, x)
    print_it(x)
    print('\nUsunięcie dwóch ostatnich elementów listy za pomocą funkcji pop:')
    for i in range(2):
        x = pop(x)
    print_it(x)
    print('\nStworzenie nowej listy zawierającej 2 pierwsze elementy listy wyjściowej za pomocą funkcji take:')
    y = take(2, x)
    print_it(y)
    print('\nStworzenie nowej listy zawierającej 2 ostatnie elementy listy wyjściowej za pomocą funkcji drop:')
    z = drop(2, x)
    print_it(z)
    print('\nDowód na to, że lista wyjściowa nie została zmieniona:')
    print_it(x)


if __name__ == "__main__":
    main()
