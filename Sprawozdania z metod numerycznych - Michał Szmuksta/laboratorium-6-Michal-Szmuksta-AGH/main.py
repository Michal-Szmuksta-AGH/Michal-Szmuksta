import numpy as np
import pickle

from typing import Union, List, Tuple


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


def log_sing_value(n: int, min_order: Union[int, float], max_order: Union[int, float]):
    """Funkcja generująca wektor wartości singularnych rozłożonych w skali logarytmiczne
    
        Parameters:
         n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
         min_order(int,float): rząd najmniejszej wartości w wektorze wartości singularnych
         max_order(int,float): rząd największej wartości w wektorze wartości singularnych
         Results:
         np.ndarray - wektor nierosnących wartości logarytmicznych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
         """
    if not (isinstance(n, int) and isinstance(min_order, (int, float)) and isinstance(max_order, (int, float))):
        return None
    if n <= 0 or min_order > max_order:
        return None
    return np.logspace(min_order, max_order, n)


def order_sing_value(n: int, order: Union[int, float] = 15, site: str = 'gre'):
    """Funkcja generująca wektor losowych wartości singularnych (n,) będących wartościami zmiennoprzecinkowymi losowanymi przy użyciu funkcji np.random.rand(n)*10. 
        A następnie ustawiająca wartość minimalną (site = 'low') albo maksymalną (site = 'gre') na wartość o  10**order razy mniejszą/większą.
    
        Parameters:
        n(np.ndarray): rozmiar wektora wartości singularnych (n,), gdzie n>0
        order(int,float): rząd przeskalowania wartości skrajnej
        site(str): zmienna wskazująca stronnę zmiany:
            - site = 'low' -> sing_value[-1] * 10**order
            - site = 'gre' -> sing_value[0] * 10**order
        
        Results:
        np.ndarray - wektor wartości singularnych o wymiarze (n,) zawierający wartości logarytmiczne na zadanym przedziale
        """
    if not (isinstance(n, int) and isinstance(order, (int, float)) and isinstance(site, str)):
        return None
    if n <= 0 or (site != 'gre' and site != 'low'):
        return None
    singular_values = np.random.rand(n) * 10
    if site == 'gre':
        singular_values[np.argmax(singular_values)] += 10 ** order
    if site == 'low':
        singular_values[np.argmin(singular_values)] -= 10 ** order
    return np.flip(np.sort(singular_values))


def create_matrix_from_A(A: np.ndarray, sing_value: np.ndarray):
    """Funkcja generująca rozkład SVD dla macierzy A i zwracająca otworzenie macierzy A z wykorzystaniem zdefiniowanego wektora warości singularnych

            Parameters:
            A(np.ndarray): rozmiarz macierzy A (m,m)
            sing_value(np.ndarray): wektor wartości singularnych (m,)


            Results:
            np.ndarray: macierz (m,m) utworzoną na podstawie rozkładu SVD zadanej macierzy A z podmienionym wektorem wartości singularnych na wektor sing_valu """
    if not (isinstance(A, np.ndarray) and isinstance(sing_value, np.ndarray)):
        return None
    m, n = A.shape
    if m != n or sing_value.shape != (m,):
        return None
    U, S, V = np.linalg.svd(A)
    return np.dot(U * sing_value, V)
