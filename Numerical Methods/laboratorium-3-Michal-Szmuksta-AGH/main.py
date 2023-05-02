import math

import numpy as np
import scipy
import pickle

from typing import Union, List, Tuple


def absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[
    int, float, np.ndarray]:
    """Obliczenie błędu bezwzględnego.
        Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.

        Parameters:
        v (Union[int, float, List, np.ndarray]): wartość dokładna
        v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona

        Returns:
        err Union[int, float, np.ndarray]: wartość błędu bezwzględnego,
                                           NaN w przypadku błędnych danych wejściowych
        """
    if not (isinstance(v, (int, float, np.ndarray, List)) and isinstance(v_aprox, (int, float, List, np.ndarray))):
        return np.nan
    if isinstance(v, List):
        v = np.array(v)
    if isinstance(v_aprox, List):
        v_aprox = np.array(v_aprox)
    if isinstance(v, np.ndarray) and isinstance(v_aprox, np.ndarray) and not (
            min(v.shape) in v_aprox.shape or max(v.shape) in v_aprox.shape):
        return np.nan
    return np.abs(v - v_aprox)


def relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray]) -> Union[
    int, float, np.ndarray]:
    """Obliczenie błędu względnego.
        Funkcja powinna działać zarówno na wartościach skalarnych, listach jak i wektorach/macierzach biblioteki numpy.

        Parameters:
        v (Union[int, float, List, np.ndarray]): wartość dokładna
        v_aprox (Union[int, float, List, np.ndarray]): wartość przybliżona

        Returns:
        err Union[int, float, np.ndarray]: wartość błędu względnego,
                                           NaN w przypadku błędnych danych wejściowych
        """
    if not (isinstance(v, (int, float, np.ndarray, List)) and isinstance(v_aprox, (int, float, List, np.ndarray))):
        return np.nan
    if isinstance(v, List):
        v = np.array(v)
    if isinstance(v_aprox, List):
        v_aprox = np.array(v_aprox)
    if isinstance(v, np.ndarray) and isinstance(v_aprox, np.ndarray) and not (
            min(v.shape) in v_aprox.shape or max(v.shape) in v_aprox.shape):
        return np.nan
    if isinstance(v, (int, float)) and v == 0:
        return np.nan
    if isinstance(v, np.ndarray) and 0 in v:
        return np.nan
    return np.divide(np.abs(v - v_aprox), v)


def p_diff(n: int, c: Union[float, int]) -> float:
    """Funkcja wylicza wartości wyrażeń P1 i P2 w zależności od n i c.
        Następnie zwraca wartość bezwzględną z ich różnicy.
        Szczegóły w Zadaniu 2.

        Parameters:
        n Union[int]:
        c Union[int, float]:

        Returns:
        diff float: różnica P1-P2
                    NaN w przypadku błędnych danych wejściowych
        """
    if not (isinstance(n, int) and isinstance(c, (float, int))):
        return np.nan
    b = 2 ** n
    P1 = b - b
    P1 = P1 + c
    P2 = b + c
    P2 = P2 - b
    return np.abs(P2 - P1)


def exponential(x: Union[int, float], n: int) -> float:
    """Funkcja znajdująca przybliżenie funkcji exp(x).
        Do obliczania silni można użyć funkcji scipy.math.factorial(x)
        Szczegóły w Zadaniu 3.

        Parameters:
        x Union[int, float]: wykładnik funkcji ekspotencjalnej
        n Union[int]: liczba wyrazów w ciągu

        Returns:
        exp_aprox float: aproksymowana wartość funkcji,
                         NaN w przypadku błędnych danych wejściowych
        """
    if not (isinstance(x, (int, float)) and isinstance(n, int)) or n < 0:
        return np.nan
    exp_aprox = 0
    for i in range(0, n):
        exp_aprox += (x ** i) / (math.factorial(i))
    return exp_aprox


def coskx1(k: int, x: Union[int, float]) -> float:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 1.
        Szczegóły w Zadaniu 4.

        Parameters:
        x Union[int, float]:
        k Union[int]:

        Returns:
        coskx float: aproksymowana wartość funkcji,
                     NaN w przypadku błędnych danych wejściowych
        """
    if not (isinstance(k, int) and isinstance(x, (float, int))):
        return np.nan
    if k < 0:
        k = np.abs(k)
    if k == 0:
        return 1
    if k == 1:
        return np.cos(x)
    else:
        return 2 * np.cos(x) * coskx1(k - 1, x) - coskx1(k - 2, x)


def coskx2(k: int, x: Union[int, float]) -> Tuple[float, float]:
    """Funkcja znajdująca przybliżenie funkcji cos(kx). Metoda 2.
    Szczegóły w Zadaniu 4.
    
    Parameters:
    x Union[int, float]:  
    k Union[int]: 
    
    Returns:
    coskx, sinkx float: aproksymowana wartość funkcji,
                        NaN w przypadku błędnych danych wejściowych
    """
    if not (isinstance(k, int) and isinstance(x, (float, int))) or k < 0:
        return np.nan

    def cos_inplace(k, x):
        if k == 0:
            return 1
        return np.cos(x) * cos_inplace(k - 1, x) - np.sin(x) * sin_inplace(k - 1, x)

    def sin_inplace(k, x):
        if k == 0:
            return 0
        return np.sin(x) * cos_inplace(k - 1, x) + np.cos(x) * sin_inplace(k - 1, x)

    # if k < 0:
    #     k = np.abs(k)
    #     return cos_inplace(k, x), (-1)*sin_inplace(k, x)
    # else:

    return cos_inplace(k, x), sin_inplace(k, x)


def pi(n: int) -> float:
    """Funkcja znajdująca przybliżenie wartości stałej pi.
    Szczegóły w Zadaniu 5.
    
    Parameters:
    n Union[int, List[int], np.ndarray[int]]: liczba wyrazów w ciągu
    
    Returns:
    pi_aprox float: przybliżenie stałej pi,
                    NaN w przypadku błędnych danych wejściowych
    """
    if not isinstance(n, int) or n <= 0:
        return np.nan
    pi_aprox = 0
    for i in range(1, n + 1):
        pi_aprox += 1 / (i ** 2)
    return np.sqrt(pi_aprox * 6)
