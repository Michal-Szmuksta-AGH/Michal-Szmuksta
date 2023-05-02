from typing import Union, List, Tuple
import numpy as np
import pandas as pandas
import scipy
import pickle


def first_spline(x: np.ndarray, y: np.ndarray):
    """Funkcja wyznaczająca wartości współczynników spline pierwszego stopnia.

    Parametrs:
    x(float): argumenty, dla danych punktów
    y(float): wartości funkcji dla danych argumentów

    return (a,b) - krotka zawierająca współczynniki funkcji linowych"""
    if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)):
        return None
    if not np.shape(x) == np.shape(y):
        return None
    a = []
    b = []
    for x_k, x_k_plus_one, y_k, y_k_plus_one in zip(x, x[1:], y, y[1:]):
        a.append((y_k_plus_one - y_k) / (x_k_plus_one - x_k))
    for x_i, y_i, a_i in zip(x, y, a):
        b.append(y_i - a_i * x_i)
    return a, b


def cubic_spline(x: np.ndarray, y: np.ndarray, tol=1e-100):
    """
    Interpolacja splajnów cubicznych

    Returns:
    b współczynnik przy x stopnia 1
    c współczynnik przy x stopnia 2
    d współczynnik przy x stopnia 3
    """
    if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)):
        return None
    if not np.shape(x) == np.shape(y):
        return None
    x = np.array(x)
    y = np.array(y)
    ### check if sorted
    if np.any(np.diff(x) < 0):
        idx = np.argsort(x)
        x = x[idx]
        y = y[idx]

    size = len(x)
    delta_x = np.diff(x)
    delta_y = np.diff(y)

    ### Get matrix A
    A = np.zeros(shape=(size, size))
    b = np.zeros(shape=(size, 1))
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, size - 1):
        A[i, i - 1] = delta_x[i - 1]
        A[i, i + 1] = delta_x[i]
        A[i, i] = 2 * (delta_x[i - 1] + delta_x[i])
        ### Get matrix b
        b[i, 0] = 3 * (delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1])

    ### Solves for c in Ac = b
    # print('Jacobi Method Output:')
    c = jacobi(A, b, np.zeros(len(A)), tol=tol, n_iterations=1000)

    ### Solves for d and b
    d = np.zeros(shape=(size - 1, 1))
    b = np.zeros(shape=(size - 1, 1))
    for i in range(0, len(d)):
        d[i] = (c[i + 1] - c[i]) / (3 * delta_x[i])
        b[i] = (delta_y[i] / delta_x[i]) - (delta_x[i] / 3) * (2 * c[i] + c[i + 1])

    return b.squeeze(), c.squeeze(), d.squeeze()


def jacobi(A, b, x0, tol, n_iterations=300):
    """
    Iteracyjne rozwiązanie równania Ax=b dla zadanego x0

    Returns:
    x - estymowane rozwiązanie
    """
    n = A.shape[0]
    x = x0.copy()
    x_prev = x0.copy()
    counter = 0
    x_diff = tol + 1

    while (x_diff > tol) and (counter < n_iterations):  # iteration level
        for i in range(0, n):  # element wise level for x
            s = 0
            for j in range(0, n):  # summation for i !=j
                if i != j:
                    s += A[i, j] * x_prev[j]

            x[i] = (b[i] - s) / A[i, i]
        # update values
        counter += 1
        x_diff = (np.sum((x - x_prev) ** 2)) ** 0.5
        x_prev = x.copy()  # use new x for next iteration

    # print("Number of Iterations: ", counter)
    # print("Norm of Difference: ", x_diff)
    return x


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
    if not (isinstance(x, np.ndarray) and isinstance(xi, np.ndarray) and isinstance(yi, np.ndarray) and isinstance(wi,
                                                                                                                   np.ndarray)):
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
