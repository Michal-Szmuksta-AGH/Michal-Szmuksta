import numpy as np
import scipy as sp
from scipy import linalg
from datetime import datetime
import pickle

from typing import Union, List, Tuple


def spare_matrix_Abt(m: int, n: int):
    """Funkcja tworząca zestaw składający się z macierzy A (m,n), wektora b (n,)  i pomocniczego wektora t (m,) zawierających losowe wartości
    Parameters:
    m(int): ilość wierszy macierzy A
    n(int): ilość kolumn macierzy A
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,n) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not (isinstance(m, int) and isinstance(n, int)):
        return None
    if m <= 0 or n <= 0:
        return None
    t = np.linspace(0, 1, m)
    b = np.cos(4 * t)
    A = np.vander(t, n)
    return np.fliplr(A), b


def square_from_rectan(A: np.ndarray, b: np.ndarray):
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników na kwadratowy układ równań. Funkcja ma zwrócić nową macierz współczynników  i nowy wektor współczynników
    Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (n,n) i wektorem (n,)
             Jeżeli dane wejściowe niepoprawne funkcja zwraca None
     """
    if not (isinstance(A, np.ndarray) and isinstance(b, np.ndarray)):
        return None
    At = np.transpose(A)
    return np.dot(At, A), np.dot(At, b)


def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,n) zawierająca współczynniki równania
      x: wektor x (n,) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów
      """
    if not (isinstance(A, np.ndarray) and isinstance(b, np.ndarray) and isinstance(x, np.ndarray)):
        return None
    m, n = A.shape
    if x.shape != (n,) or b.shape != (m,):
        return None
    return np.linalg.norm(np.matmul(A, x) - b)
