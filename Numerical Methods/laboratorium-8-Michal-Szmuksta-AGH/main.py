import numpy as np
import scipy as sp
import pickle

from typing import Union, List, Tuple, Optional


def diag_dominant_matrix_A_b(m: int) -> Union[Tuple[np.ndarray, np.ndarray], None]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Macierz A ma być diagonalnie zdominowana, tzn. wyrazy na przekątnej sa wieksze od pozostałych w danej kolumnie i wierszu
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: macierz diagonalnie zdominowana o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(m, int) or m < 1:
        return None
    A = np.random.randint(0, 9, (m, m))
    b = np.random.randint(0, 9, (m,))
    diag = np.random.randint(9 * m, 90 * m, (m,))
    np.fill_diagonal(A, diag)
    return A, b


def is_diag_dominant(A: np.ndarray) -> Union[bool, None]:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest diagonalnie zdominowana
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(A, np.ndarray):
        return None
    if len(A.shape) != 2:
        return None
    if A.shape[0] != A.shape[1]:
        return None
    diag = np.diag(np.abs(A))
    row_sum = np.sum(abs(A), axis=1) - diag
    col_sum = np.sum(abs(A), axis=0) - diag
    if np.all(diag > row_sum) and np.all(diag > col_sum):
        return True
    else:
        return False


def symmetric_matrix_A_b(m: int) -> Union[Tuple[np.ndarray, np.ndarray], None]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych z przedziału 0, 9
    Parameters:
    m int: wymiary macierzy i wektora
    
    Returns:
    Tuple[np.ndarray, np.ndarray]: symetryczną macierz o rozmiarze (m,m) i wektorem (m,)
                                   Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(m, int) or m < 1:
        return None
    K = np.random.randint(0, 9, (m, m))
    b = np.random.randint(0, 9, (m,))
    A = np.tril(K) + np.tril(K, -1).T
    return A, b


def is_symmetric(A: np.ndarray) -> Union[bool, None]:
    """Funkcja sprawdzająca czy macierzy A (m,m) jest symetryczna
    Parameters:
    A np.ndarray: macierz wejściowa
    
    Returns:
    bool: sprawdzenie warunku 
          Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(A, np.ndarray):
        return None
    if len(A.shape) != 2:
        return None
    if A.shape[0] != A.shape[1]:
        return None
    return np.all(A == A.T)


def solve_jacobi(A: np.ndarray, b: np.ndarray, x_init: np.ndarray,
                 epsilon: Optional[float] = 1e-16, maxiter: Optional[int] = 100) -> Union[Tuple[np.ndarray, int], None]:
    """Funkcja tworząca zestaw składający się z macierzy A (m,m), wektora b (m,) o losowych wartościach całkowitych
    Parameters:
    A np.ndarray: macierz współczynników
    b np.ndarray: wektor wartości prawej strony układu
    x_init np.ndarray: rozwiązanie początkowe
    epsilon Optional[float]: zadana dokładność
    maxiter Optional[int]: ograniczenie iteracji
    
    Returns:
    np.ndarray: przybliżone rozwiązanie (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    int: iteracja
    """
    if not (isinstance(A, np.ndarray) and isinstance(b, np.ndarray) and isinstance(x_init, np.ndarray) and isinstance(
            epsilon, float) and isinstance(maxiter, int)):
        return None
    if epsilon < 0 or maxiter < 1:
        return None
    if A.shape[0] != A.shape[1] or b.shape[0] != A.shape[0] or x_init.shape[0] != A.shape[0]:
        return None
    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    D_inv = np.diag(1 / np.diag(D))
    for i in range(maxiter):
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        r_norm = np.linalg.norm(x_new - x)
        if r_norm < epsilon:
            return x_new, i
        x = x_new
    return x, maxiter


def random_matrix_Ab(m: int, limit=1000):
    """Funkcja tworząca zestaw składający się z macierzy A (m,m) i wektora b (m,)  zawierających losowe wartości
    Parameters:
    m(int): rozmiar macierzy
    Results:
    (np.ndarray, np.ndarray): macierz o rozmiarze (m,m) i wektorem (m,)
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(m, int) or m < 0:
        return None
    return np.random.randint(0, limit, (m, m)), np.random.randint(0, 1000, (m,))


def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray):
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

      Parameters:
      A: macierz A (m,m) zawierająca współczynniki równania
      x: wektor x (m.) zawierający rozwiązania równania
      b: wektor b (m,) zawierający współczynniki po prawej stronie równania

      Results:
      (float)- wartość normy residuom dla podanych parametrów"""
    if not (isinstance(A, np.ndarray) and isinstance(b, np.ndarray) and isinstance(x, np.ndarray)):
        return None
    m, n = A.shape
    if m != n or x.shape != (m,) or b.shape != (m,):
        return None
    return np.linalg.norm(np.matmul(A, x) - b)



