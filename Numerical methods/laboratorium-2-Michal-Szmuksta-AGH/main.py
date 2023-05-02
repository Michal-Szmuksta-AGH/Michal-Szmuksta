import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random


def compare_plot(x1: np.ndarray, y1: np.ndarray, x2: np.ndarray, y2: np.ndarray,
                 xlabel: str, ylabel: str, title: str, label1: str = '$f(x)$',
                 label2: str = 'g(x)') -> matplotlib.pyplot.figure:
    if x1.shape != y1.shape or min(x1.shape) == 0 or x2.shape != y2.shape or min(x2.shape) == 0:
        return None
    fig, ax = plt.subplots()
    ax.plot(x1, y1, color='b', linewidth=4)
    ax.plot(x2, y2, color='r', linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend([label1, label2])
    ax.grid('on')
    ax.axis([min(min(x1), min(x2)), max(max(x1), max(x2)), min(min(y1), min(y2)), max(max(y1), max(y2))])
    return fig

    """Funkcja służąca do porównywania dwóch wykresów typu plot. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    label1(str): nazwa serii z pierwszego wykresu,
    label2(str): nazwa serii z drugiego wykresu.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 3 
    """


def parallel_plot(x1: np.ndarray, y1: np.ndarray, x2: np.ndarray, y2: np.ndarray,
                  x1label: str, y1label: str, x2label: str, y2label: str, title: str, orientation: str):
    if x1.shape != y1.shape or min(x1.shape) == 0 or x2.shape != y2.shape or min(x2.shape) == 0\
            or (orientation != '|' and orientation != '-'):
        return None
    if orientation == '|':
        rows = 1
        columns = 2
    if orientation == '-':
        rows = 2
        columns = 1
    fig, (ax1, ax2) = plt.subplots(nrows=rows, ncols=columns)
    fig.tight_layout(pad=2)
    ax1.plot(x1, y1)
    ax2.plot(x2, y2)
    ax1.set(xlabel=x1label, ylabel=y1label)
    ax2.set(xlabel=x2label, ylabel=y2label)
    fig.suptitle(title)
    ax1.set_box_aspect(1)
    ax2.set_box_aspect(1)
    return fig

    """Funkcja służąca do stworzenia dwóch wykresów typu plot w konwencji subplot wertykalnie lub chorycontalnie. 
    Szczegółowy opis w zadaniu 5.
    
    Parameters:
    x1(np.ndarray): wektor wartości osi x dla pierwszego wykresu,
    y1(np.ndarray): wektor wartości osi y dla pierwszego wykresu,
    x2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    y2(np.ndarray): wektor wartości osi x dla drugiego wykresu,
    x1label(str): opis osi x dla pierwszego wykresu,
    y1label(str): opis osi y dla pierwszego wykresu,
    x2label(str): opis osi x dla drugiego wykresu,
    y2label(str): opis osi y dla drugiego wykresu,
    title(str): tytuł wykresu,
    orientation(str): parametr przyjmujący wartość '-' jeżeli subplot ma posiadać dwa wiersze albo '|' jeżeli ma posiadać dwie kolumny.

    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x1,y1), (x2,y2) zgody z opisem z zadania 5
    """


def log_plot(x: np.ndarray, y: np.ndarray, xlabel: str, ylabel: str, title: str, log_axis: str):
    if x.shape != y.shape or min(x.shape) == 0:
        return None
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid('on')
    if log_axis == 'x':
        ax.set_xscale('log')
    if log_axis == 'y':
        ax.set_yscale('log')
    if log_axis == 'xy':
        ax.set_xscale('log')
        ax.set_yscale('log')
    return fig

    """Funkcja służąca do tworzenia wykresów ze skalami logarytmicznymi. 
    Szczegółowy opis w zadaniu 7.
    
    Parameters:
    x(np.ndarray): wektor wartości osi x,
    y(np.ndarray): wektor wartości osi y,
    xlabel(str): opis osi x,
    ylabel(str): opis osi y,
    title(str): tytuł wykresu ,
    log_axis(str): wartość oznacza:
        - 'x' oznacza skale logarytmiczną na osi x,
        - 'y' oznacza skale logarytmiczną na osi y,
        - 'xy' oznacza skale logarytmiczną na obu osiach.
    
    Returns:
    matplotlib.pyplot.figure: wykres zbiorów (x,y) zgody z opisem z zadania 7 
    """
