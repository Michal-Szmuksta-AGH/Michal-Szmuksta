import pytest
from app import bubble_sort

def test_normal_case_1():
    got = bubble_sort([1,10,3,4,5,6,7,8,9,2])
    want = ([1,2,3,4,5,6,7,8,9,10], 15)

    assert got == want

def test_normal_case_2():
    got = bubble_sort([2,1,4,3,6,5,8,7,10,9])
    want = ([1,2,3,4,5,6,7,8,9,10], 5)

    assert got == want

def test_best_case():
    got = bubble_sort([1,2,3,4,5,6,7,8,9,10])
    want = ([1,2,3,4,5,6,7,8,9,10], 0)

    assert got == want

def test_worst_case():
    got = bubble_sort([10,9,8,7,6,5,4,3,2,1])
    want = ([1,2,3,4,5,6,7,8,9,10], 45)

    assert got == want