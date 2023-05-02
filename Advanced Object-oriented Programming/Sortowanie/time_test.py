#!/usr/bin/python
# -*- coding: utf-8 -*-
import sort, random, sys
from timeit import timeit

list_sorted = [x for x in range(1, 1001)]
print(list_sorted)
list_sorted_inversely = [x for x in range(1000, 0, -1)]
print(list_sorted_inversely)
list_with_the_same_values = 1000 * [500]
print(list_with_the_same_values)
list_with_random_values = random.sample(range(1, 1001), 1000)
print(list_with_random_values)
print(len(list_with_random_values), len(list_with_the_same_values), len(list_sorted_inversely), len(list_sorted))

print('')
print('Test sortowania bąbelkowego:')
print('')

test_bubblesort__list_sorted = timeit('sort.bubblesort(list_sorted)', number=1000, globals=globals())/1000
print('Posortowana lista (średnie jedno pełne wykonanie algorytmu): ',test_bubblesort__list_sorted, 's')
test_bubblesort__list_sorted_inversely = timeit('sort.bubblesort(list_sorted_inversely)', number=1000, globals=globals())/1000
print('Lista posortowana w odwrotnej kolejności (średnie jedno pełne wykonanie algorytmu): ',test_bubblesort__list_sorted_inversely, 's')
test_bubblesort__list_with_the_same_values = timeit('sort.bubblesort(list_with_the_same_values)',number=1000,globals=globals())/1000
print('Lista z równymi wartościami (średnie jedno pełne wykonanie algorytmu): ',test_bubblesort__list_with_the_same_values, 's')
test_bubblesort__list_with_random_values = timeit('sort.bubblesort(list_with_random_values)',number=1000,globals=globals())/1000
print('Lista z losowymi wartościami (średnie jedno pełne wykonanie algorytmu): ',test_bubblesort__list_with_random_values, 's')

print('')
print('Test algorytmu quicksort:')
print('')

sys.setrecursionlimit(1500)
test_quicksort__list_sorted = timeit('sort.quicksort(list_sorted)', number=1000, globals=globals())/1000
print('Posortowana lista (średnie jedno pełne wykonanie algorytmu): ',test_quicksort__list_sorted,'s')
test_quicksort__list_sorted_inversely = timeit('sort.quicksort(list_sorted_inversely)', number=1000, globals=globals())/1000
print('Lista posortowana w odwrotnej kolejności (średnie jedno pełne wykonanie algorytmu): ',test_quicksort__list_sorted_inversely,'s')
test_quicksort__list_with_the_same_values = timeit('sort.quicksort(list_with_the_same_values)',number=1000,globals=globals())/1000
print('Lista z równymi wartościami (średnie jedno pełne wykonanie algorytmu): ',test_quicksort__list_with_the_same_values,'s')
test_quicksort__list_with_random_values = timeit('sort.quicksort(list_with_random_values)',number=1000,globals=globals())/1000
print('Lista z losowymi wartościami (średnie jedno pełne wykonanie algorytmu): ',test_quicksort__list_with_random_values,'s')

#Wnioski:

#Testy czasowe potwierdzają wiedzę teoretyczną dotyczącą złożoności czasowej algorytmów.
#Sortowanie bąbelkowe wykazuje złożoność liniową gdy lista jest posortowana lub posiada identyczne elementy (czyli też jest posortowana),
#w pozostałych przypadkach czas potrzebny na posortowanie listy ma charakter kwadratowy.
#(gdy lista jest posortowana na odwerót ilość potrzebnego czasu jest oczywiście większa).

#Algorytm quicksort wykazuje kwadratową złożoność czasową gdy jako pivot wybierany jest największy lub najmniejszy element
#(lista posortowana lub lista posortowana w odwrotnej kolejności)
#Gdy do posortowania dana jest lista z równymi wartościami lub posortowana lista, algorytm wykazuje złożoność wyrażoną wzorem nlog(n)
#Gdzie n to liczba elementów listy

#Co ciekawe algorytm quicksort w przypadku pesymistycznym sortuje szybciej niż algorytm bubblesort w przypadku optymistycznym mimo takiej samej złożoności czasowej.
#Wynika to najprawdopodobniej współczynnika w wzorze określającym dokładnie czas niezbędny do wykonania obliczeń, który może być większy dla sortowania bąbelkowego

