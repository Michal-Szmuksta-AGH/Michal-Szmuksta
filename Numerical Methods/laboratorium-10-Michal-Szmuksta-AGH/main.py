import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from numpy.core._multiarray_umath import ndarray
from numpy.polynomial import polynomial as P
import pickle


# zad1
def polly_A(x: np.ndarray):
    """Funkcja wyznaczajaca współczynniki wielomianu przy znanym wektorze pierwiastków.
    Parameters:
    x: wektor pierwiastków
    Results:
    (np.ndarray): wektor współczynników
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(x, np.ndarray):
        return None
    return P.polyfromroots(x)


def roots_20(a: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray): wektor współczynników i miejsc zerowych w danej pętli
                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(a, np.ndarray):
        return None
    samples = np.random.random_sample((len(a),)) * 10e-10
    a_new = a + np.array(samples)
    return a_new, P.polyroots(a_new)


# zad 2

def frob_a(wsp: np.ndarray):
    """Funkcja zaburzająca lekko współczynniki wielomianu na postawie wyznaczonych współczynników wielomianu
        oraz zwracająca dla danych współczynników, miejsca zerowe wielomianu funkcją polyroots.
    Parameters:
    a: wektor współczynników
    Results:
    (np.ndarray, np. ndarray, np.ndarray, np. ndarray,): macierz Frobenusa o rozmiarze nxn, gdzie n-1 stopień wielomianu,
    wektor własności własnych, wektor wartości z rozkładu schura, wektor miejsc zerowych otrzymanych za pomocą funkcji polyroots

                Jeżeli dane wejściowe niepoprawne funkcja zwraca None
    """
    if not isinstance(wsp, np.ndarray):
        return None
    frob = np.eye(len(wsp) - 1)
    zero_vec = np.zeros((len(wsp) - 1, 1))
    frob = np.concatenate((zero_vec, frob), axis=1)
    new_wsp = np.reshape(-wsp, (1, len(wsp)))
    frob = np.concatenate((frob, new_wsp), axis=0)
    return frob, np.linalg.eigvals(frob), scipy.linalg.schur(frob), P.polyroots(wsp)
