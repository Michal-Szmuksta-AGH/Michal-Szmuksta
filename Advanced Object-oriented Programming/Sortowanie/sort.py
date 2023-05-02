# Michał Szmuksta , 406376
from typing import Tuple


def quicksort(input_list_q: list, start_q: int = 0, stop_q: int = -1) -> list:
    output_list = input_list_q.copy()
    if stop_q == -1:
        stop_q = len(input_list_q) - 1

    def quicksort_inplace(input_list: list, start: int, stop: int) -> None:
        pivot = input_list[start]
        i = start
        j = stop
        while i < j:
            while input_list[i] < pivot:
                i += 1
            while input_list[j] > pivot:
                j -= 1
            if i <= j:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                i += 1
                j -= 1
        if start < j:
            quicksort_inplace(input_list, start, j)
        if i < stop:
            quicksort_inplace(input_list, i, stop)

    quicksort_inplace(output_list, start_q, stop_q)
    return output_list


def bubblesort(input_list: list) -> Tuple[list, int]:
    output_list = input_list.copy()
    n = len(output_list)
    num_of_comparisons = 0
    sem = 0
    while n > 1 and sem == 0:
        sem = 1
        for i in range(1, n):
            num_of_comparisons += 1
            if output_list[i - 1] > output_list[i]:
                output_list[i - 1], output_list[i] = output_list[i], output_list[i - 1]
                sem = 0
        n -= 1
    return output_list, num_of_comparisons
