def bubble_sort(arr):
    # Argumenty:
    # - arr - tablica typu list do posortowania, zawierająca elementy typu int lub float

    # Wartości zwracane:
    # arr - posortowana tablica arr w porządku rosnącym
    # swaps - liczba zamian wykonanych przez algorytm

    n = len(arr)
    swapped = False
    swaps = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                if not swapped:
                    # Jeśli algorytm nie wykonał żadnej zamiany podczas iterowania po tablicy
                    # wówczas jest ona posortowana i można zakończyć działanie funkcji
                    return arr, swaps
    return arr, swaps