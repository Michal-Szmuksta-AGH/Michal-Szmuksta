import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle
from inspect import isfunction

from typing import Union, List, Tuple


def fun(x):
    return np.exp(-2 * x) + x ** 2 - 1


def dfun(x):
    return -2 * np.exp(-2 * x) + 2 * x


def ddfun(x):
    return 4 * np.exp(-2 * x) + 2


def bisection(a: Union[int, float], b: Union[int, float], f: typing.Callable[[float], float], epsilon: float,
              iteration: int) -> Union[Tuple[float, int], None]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(
            iteration, int) and isinstance(f, typing.Callable)):
        return None
    if a >= b or iteration <= 0 or np.sign(f(a)) == np.sign(f(b)):
        return None
    it = 0
    while abs(a - b) > epsilon and it < iteration:
        x = (a + b) / 2
        if abs(f(x)) <= epsilon:
            break
        if f(x) * f(a) <= 0:
            b = x
        else:
            a = x
        it = it + 1
    return (a + b) / 2, it


def secant(a: Union[int, float], b: Union[int, float], f: typing.Callable[[float], float], epsilon: float,
           iteration: int) -> Union[Tuple[float, int], None]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(
            iteration, int) and isinstance(f, typing.Callable)):
        return None
    if a >= b or iteration <= 0 or np.sign(f(a)) == np.sign(f(b)):
        return None
    it = 0
    while abs(a - b) > epsilon and it < iteration:
        x = (f(b) * a - f(a) * b) / (f(b) - f(a))
        if abs(f(x)) <= epsilon:
            break
        if f(x) * f(a) >= 0:
            a = x
        if f(x) * f(b) > 0:
            b = x
        it = it + 1
    return (f(b) * a - f(a) * b) / (f(b) - f(a)), it


def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float],
           ddf: typing.Callable[[float], float], a: Union[int, float], b: Union[int, float], epsilon: float,
           iteration: int) -> Union[Tuple[float, int], None]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(
            iteration, int) and isinstance(f, typing.Callable) and isinstance(df, typing.Callable) and isinstance(ddf,
            typing.Callable)):
        return None
    if a >= b or iteration <= 0 or np.sign(f(a)) == np.sign(f(b)):
        return None
    x = np.linspace(a, b, 1000)
    if not ((np.all(np.sign(df(x)) < 0) or np.all(np.sign(df(x)) > 0)) and (np.all(np.sign(ddf(x)) < 0) or np.all(np.sign(ddf(x)) > 0))):
        return None
    it = 0
    xk = b
    x = a
    while it < iteration:
        x = xk - (f(xk) / df(xk))
        if abs(x - xk) <= epsilon:
            break
        xk = x
        it = it + 1
    return xk, it