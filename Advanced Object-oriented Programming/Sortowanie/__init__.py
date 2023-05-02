# Pozostaw ten plik pusty, ew. wykorzystaj do własnych testów.
import sort
import random

a = [4, 4, 5, 674, 4, 7, 98, 2, 1, 32, 3, 4, 65, 3, 4, 3, 22, 5, 25, 3, 53, 6, 8, 9, 9, 856737, 2,
     2, 1, 3, 3, 5, 6, 8, 89, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
d = [10, 2, 3]
e = random.sample(range(0, 1000), 1000)
f = [5, 2, 3, 1, 4]
print(a)
print(sort.quicksort(a))
print(a)
print(sort.bubblesort(a))
print(a)
print(sort.quicksort(e))
print(e)
print(sort.bubblesort(b))
print('')
print(sort.bubblesort(f))
