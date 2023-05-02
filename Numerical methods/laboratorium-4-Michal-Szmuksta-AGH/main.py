##
import numpy as np
import scipy
import pickle
import matplotlib.pyplot as plt

from typing import Union, List, Tuple


def chebyshev_nodes(n: int = 10) -> Union[np.ndarray, None]:
    """Funkcja tworząca wektor zawierający węzły czybyszewa w postaci wektora (n+1,)
    
    Parameters:
    n(int): numer ostaniego węzła Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(n, int) or n <= 0:
        return None
    v = []
    for x in range(0, n + 1):
        v.append(np.cos(x * np.pi / n))
    return np.array(v)


def bar_czeb_weights(n: int = 10) -> Union[np.ndarray, None]:
    """Funkcja tworząca wektor wag dla węzłów czybyszewa w postaci (n+1,)
    
    Parameters:
    n(int): numer ostaniej wagi dla węzłów Czebyszewa. Wartość musi być większa od 0.
     
    Results:
    np.ndarray: wektor wag dla węzłów Czybyszewa o rozmiarze (n+1,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(n, int) or n <= 0:
        return None

    def delta(j, n):
        if j == 0 or j == n:
            return 0.5
        if n > j > 0:
            return 1

    w = []
    for j in range(0, n + 1):
        w.append(((-1) ** j) * delta(j, n))
    return np.array(w)


def barycentric_inte(xi: np.ndarray, yi: np.ndarray, wi: np.ndarray, x: np.ndarray) -> Union[np.ndarray, None]:
    """Funkcja przprowadza interpolację metodą barycentryczną dla zadanych węzłów xi
        i wartości funkcji interpolowanej yi używając wag wi. Zwraca wyliczone wartości
        funkcji interpolującej dla argumentów x w postaci wektora (n,) gdzie n to dłógość
        wektora n. 
    
    Parameters:
    xi(np.ndarray): węzły interpolacji w postaci wektora (m,), gdzie m > 0
    yi(np.ndarray): wartości funkcji interpolowanej w węzłach w postaci wektora (m,), gdzie m>0
    wi(np.ndarray): wagi interpolacji w postaci wektora (m,), gdzie m>0
    x(np.ndarray): argumenty dla funkcji interpolującej (n,), gdzie n>0 
     
    Results:
    np.ndarray: wektor wartości funkcji interpolujący o rozmiarze (n,). 
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not (isinstance(x, np.ndarray) and isinstance(xi, np.ndarray) and isinstance(yi, np.ndarray) and isinstance(wi, np.ndarray)):
        return None
    if xi.shape != yi.shape or yi.shape != wi.shape or wi.shape != xi.shape:
        return None
    Y = []
    for x_iter in x:
        Nominator = 0
        Denominator = 0
        if not x_iter in xi:
            for xi_iter, yi_iter, wi_iter in zip(xi, yi, wi):
                Nominator += (yi_iter * wi_iter) / (x_iter - xi_iter)
                Denominator += wi_iter / (x_iter - xi_iter)
            Y.append(Nominator / Denominator)
        else:
            Y.append(yi[np.where(xi == x_iter)[0][0]])
    Y = np.array(Y)
    return Y


def L_inf(xr: Union[int, float, List, np.ndarray], x: Union[int, float, List, np.ndarray]) -> float:
    """Obliczenie normy  L nieskończonośćg. 
    Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach biblioteki numpy.
    
    Parameters:
    xr (Union[int, float, List, np.ndarray]): wartość dokładna w postaci wektora (n,)
    x (Union[int, float, List, np.ndarray]): wartość przybliżona w postaci wektora (n,1)
    
    Returns:
    float: wartość normy L nieskończoność,
                                    NaN w przypadku błędnych danych wejściowych
    """
    if not (isinstance(xr, (int, float, List, np.ndarray)) and isinstance(x, (int, float, List, np.ndarray))):
        return np.NaN
    if np.shape(xr) != np.shape(x):
        return np.NaN
    if isinstance(x, (List, np.ndarray)):
        return max(np.abs(np.subtract(xr, x)))
    else:
        return np.abs(xr - x)
