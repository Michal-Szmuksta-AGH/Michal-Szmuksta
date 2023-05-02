import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

from sqlalchemy import create_engine

# connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)
connection = db.connect()


def film_in_category(category_id: int) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if not isinstance(category_id, int):
        return None
    else:
        df = pd.read_sql("SELECT fi.title, la.name AS languge, ca.name AS category FROM film AS fi "
                         "INNER JOIN film_category AS fc ON fc.film_id = fi.film_id "
                         "INNER JOIN category AS ca ON ca.category_id = fc.category_id "
                         "INNER JOIN language AS la ON la.language_id = fi.language_id "
                         "WHERE ca.category_id = {} ORDER BY fi.title, languge".format(category_id), con=connection)
        return df


def number_films_in_category(category_id: int) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if not isinstance(category_id, int):
        return None
    else:
        df = pd.read_sql("SELECT "
                         "ca.name AS category, COUNT(*) FROM film_category AS fc "
                         "INNER JOIN category AS ca ON ca.category_id = fc.category_id "
                         "WHERE ca.category_id = {} GROUP BY ca.name".format(category_id), con=connection)
        return df


def number_film_by_length(min_length: Union[int, float] = 0, max_length: Union[int, float] = 1e6):
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(min_length, (int, float)) or not isinstance(max_length, (int, float)) or min_length > max_length:
        return None
    else:
        df = pd.read_sql("SELECT length, COUNT(*) FROM film AS f "
                         "WHERE f.length BETWEEN {} AND {} GROUP BY f.length".format(min_length, max_length),
                         con=connection)
        return df


def client_from_city(city: str) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(city, str):
        return None
    else:
        df = pd.read_sql("SELECT ci.city, cu.first_name, cu.last_name FROM customer AS cu "
                         "INNER JOIN address AS ad ON ad.address_id = cu.address_id "
                         "INNER JOIN city AS ci ON ci.city_id = ad.city_id "
                         "WHERE ci.city = '{}'".format(city), con=connection)
        return df


def avg_amount_by_length(length: Union[int, float]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(length, (int, float)):
        return None
    else:
        df = pd.read_sql("SELECT length, AVG(pa.amount) FROM film AS fi "
                         "INNER JOIN inventory AS inv ON inv.film_id = fi.film_id "
                         "INNER JOIN rental AS re ON re.inventory_id = inv.inventory_id "
                         "INNER JOIN payment AS pa ON pa.rental_id = re.rental_id "
                         "WHERE length = {} GROUP BY length".format(length), con=connection)
        return df


def client_by_sum_length(sum_min: Union[int, float]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(sum_min, (int, float)):
        return None
    else:
        df = pd.read_sql("SELECT first_name, last_name, SUM(fi.length) FROM customer AS cu "
                         "INNER JOIN rental AS re ON re.customer_id = cu.customer_id "
                         "INNER JOIN inventory AS inv ON inv.inventory_id = re.inventory_id "
                         "INNER JOIN film AS fi ON fi.film_id = inv.film_id "
                         "GROUP BY first_name, last_name "
                         "HAVING SUM(fi.length) > {} "
                         "ORDER BY SUM(fi.length), cu.last_name".format(sum_min), con=connection)
        return df


def category_statistic_length(name: str) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(name, str):
        return None
    else:
        df = pd.read_sql(
            "SELECT name AS category, AVG(fi.length), SUM(fi.length), MIN(fi.length), MAX(fi.length) FROM category AS ca "
            "INNER JOIN film_category AS fc ON fc.category_id = ca.category_id "
            "INNER JOIN film AS fi ON fi.film_id = fc.film_id "
            "WHERE name = '{}' GROUP BY name".format(name), con=connection)
        return df
