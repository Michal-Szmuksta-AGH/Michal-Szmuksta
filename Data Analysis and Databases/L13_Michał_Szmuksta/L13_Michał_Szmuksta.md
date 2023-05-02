# Faza Zielona
W fazie zielonej napisano cztery testy mające na celu zbadanie poporawności działania algorytmu sortowania bąbelkowego:

![](./images/1.png)

Następnie zaimplementowano sam algorytm:

![](./images/2.png)

W ostatnim kroku w tej fazie uruchomiono testy, które pokazały, że algorytm działa niepoprawnie z względu na ilość zwracanych elementów:

![](./images/3.png)

# Faza Czerwona
Po analizie kodu okazało się, że zaimplementowany algorytm nie zwracał liczby zamian podczas sortowania. Dodano tą funkcjonalność:

![](./images/4.png)

Następnie ponownie uruchomiono testy, które tym razem pokazały, że algorytm działa poprawnie:

![](./images/5.png)

# Faza Refactor
Do działającego poprawnie algorytmu dodano dodatkowy warunek przyspieszający jego działanie i dodatkowe komentarze:

![](./images/6.png)