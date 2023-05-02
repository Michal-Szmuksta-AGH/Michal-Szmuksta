# **Laboratorium 6**
Michał Szmuksta, gr. 7, czwartek 10:00

#### **Wstęp**
Celem laboratorium było stworzenie prostego projektu zawierającego analizę bazy danych zawierającej informacje o zakupie odkurzaczy w pewnej sieci sklepów w województwie wielkopolskim, wykorzystując zasady protokołu TIER 3.0 oraz Tidy Data. Poniższy skrypt miał na celu analizę przetworzonych już danych zawartych w katalogu Analysis Data. W analizie danych skorzystano z biblioteki pandas w celu rozszerzenia umiejętności z zakresu analizy danych w języku Python. Poniżej zaimportowano niezbędne biblioteki.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Poniżej wczytano przygotowany do analizy zbiór danych.


```python
Wielkopolskie = pd.read_csv("../Analysis Data/14_WIELKOPOLSKIE_final.csv")
Wielkopolskie
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dni od zakupu</th>
      <th>Marka</th>
      <th>Wiek kupującego</th>
      <th>Płeć kupującego</th>
      <th>Ocena</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>Electrolux</td>
      <td>41.0</td>
      <td>M</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>Electrolux</td>
      <td>57.0</td>
      <td>M</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>Beko</td>
      <td>35.0</td>
      <td>M</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>Beko</td>
      <td>53.0</td>
      <td>M</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Electrolux</td>
      <td>27.0</td>
      <td>K</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>453</th>
      <td>2</td>
      <td>Dyson</td>
      <td>39.0</td>
      <td>M</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>454</th>
      <td>8</td>
      <td>Samsung</td>
      <td>39.0</td>
      <td>M</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>455</th>
      <td>9</td>
      <td>Electrolux</td>
      <td>26.0</td>
      <td>K</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>456</th>
      <td>6</td>
      <td>Beko</td>
      <td>43.0</td>
      <td>M</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>457</th>
      <td>9</td>
      <td>Electrolux</td>
      <td>57.0</td>
      <td>K</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>
<p>458 rows × 5 columns</p>
</div>



#### **Analiza danych**
##### **1. Rozkład liczby dni, po której klienci wystawiali ocenę**


```python
fig, ax = plt.subplots(figsize=(8, 5))
bins = range(17)
Wielkopolskie.hist(column='Dni od zakupu', rwidth = 0.618, color='r',bins=bins, ax=ax)
ax.set_xticks([(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])])
ax.set_xticklabels(range(16))
ax.set_title('Histogram klientów, którzy wystawili ocenę po danym okresie czasu')
ax.set_xlabel('Liczba dni od zakupu')
ax.set_ylabel('Liczba klientów')
ax.grid(False)
plt.show()
```


    
![png](output_6_0.png)
    


Na powyższym histogramie można zauważyć, że liczba dni od zakupu ma w przybliżeniu rozkład normalny. Najwięcej klientów decyduje się na wystawienie recenzji tydzień po zakupie. Tendencja na wykresie wskazuje, że jeśli klient tej sieci sklepów w województwie wielkopolskim nie wystawił recenzji odkurzacza w czasie 15 dni od zakupu, to z bardzo dużą pewnością można powiedzieć, że nie wystawi jej wcale.

##### **2. Liczba sprzedanych odkurzaczy w zależności od producenta**


```python
fig, ax = plt.subplots(figsize=(7, 7))
Df = Wielkopolskie.groupby(['Marka']).size()
Df_list = Df.to_list()

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:d} szt.\n{:.1f}%".format(absolute,pct)

Df.plot.pie(column='Marka',autopct=lambda pct: func(pct, Df_list), ax=ax)
ax.set_title('Liczba sprzedanych odkurzaczy w zależności od firmy')
ax.set_ylabel('')
ax.set
plt.show()
```


    
![png](output_9_0.png)
    


Powyższy wykres obrazuje, że największy udział w tej sieci sklepów w Wielkopolskim rynku sprzedanych odkurzaczy posiada firma Electrolux, zaś najmniejszy firma Samsung. Firma Beko, pomimo że jest drugim co do wielkości dystrybutorem odkurzaczy, to jej udział jest około o połowę mniejszy niż Electroluxa. Firma Tafel i Dyson posiada podobne udziały w sprzedanych odkurzaczach i stanowi on około 13-15 %.

##### **3. Rozkład wieku osób kupujących odkurzacz**


```python
fig, ax = plt.subplots(figsize=(8, 5))
bins = range(82)
Wielkopolskie.hist(column='Wiek kupującego', rwidth = 0.618, color='b',bins = bins, ax=ax)
ax.set_xticks([(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])])
ax.set_xticklabels([i if i % 5 == 0 else None for i in range(81)])
ax.set_title('Histogram wieku klientów, którzy kupili odkurzacz')
ax.set_xlabel('Wiek klienta')
ax.set_ylabel('Liczba klientów')
ax.grid(False)
plt.show()
```


    
![png](output_12_0.png)
    


Ponownie jak w przypadku pierwszego histogramu można zauważyć, że rozkład wieku kupujących odkurzacze w rozważanej sieci sklepów w Wielkopolsce jest w przybliżeniu normalny. Najwięcej kupujących ma około 40 lat. Najmłodsi kupujący są pełnoletni, zaś najstarsi skończyli 70 lat. Na histogramie można zauważyć tendencję, że poza osobami w średnim wieku, to młodsi kupują więcej odkurzaczy niż osoby starsze, co może być wynikiem wyprowadzania się przez nich do nowego miejsca zamieszkania.

##### **4. Liczba osób kupujących odkurzacz danej marki z podziałem na płeć klienta**


```python
Df1 = Wielkopolskie.loc[Wielkopolskie['Płeć kupującego'] == 'M'].groupby(['Marka']).size()
Df2 = Wielkopolskie.loc[Wielkopolskie['Płeć kupującego'] == 'K'].groupby(['Marka']).size()
Df = pd.concat([Df1, Df2], axis=1, ignore_index=True)
fig, ax = plt.subplots(figsize=(8, 5))
Df.plot.bar(ax=ax, color=['orange','magenta'])
plt.legend(['Mężczyzna','Kobieta'])
plt.title('Liczba klientów kupujących odkurzacz danej firmy w zależności od płci')
plt.xlabel('')
plt.ylabel('Liczba klientów')
plt.show()
```


    
![png](output_15_0.png)
    


Na powyższym wykresie można zauważyć, że w sklepach rozważanej sieci w Wielkopolsce to panowie zdecydowanie częściej zajmują się kupnem odkurzaczy niż kobiety. Stosunek liczby panów do liczby pań decydujących się na zakup odkurzacza danej firmy jest na oko podobny dla każdej marki, z pominięciem firmy Beko gdzie bardziej dominują mężczyźni. Co ciekawe u największego dystrybutora odkurzaczy tej sieci w Wielkopolsce - Electroluxa liczba zakupionych odkurzaczy przez panie przekracza nawet liczbę odkurzaczy zakupionych przez panów dla najmniejszego dystrybutora - Samsunga.

##### **5. Średnia ocen kupujących odkurzacze w zależności od marki produktu**


```python
Df = Wielkopolskie.groupby(['Marka']).mean()['Ocena']
fig, ax = plt.subplots(figsize=(8, 5))
Df.plot.barh(ax=ax, color='g')
ax.bar_label(ax.containers[0],fmt='%.2f')
plt.title('Wykres zależności średniej oceny odkurzaczy w zależności od marki')
plt.xlabel('Średnia ocena produktu')
plt.ylabel('')
plt.show()
```


    
![png](output_18_0.png)
    


Na powyższym wykresie można zaobserwować, że średnia ocena odkurzaczy danej firmy w tej sieci sklepów w Wielkopolsce jest bardzo podobna i oscyluje wokół wartości 2.4 / 5. Tendencja wskazuje, że odkurzacze firmy Tafel, Electrolux oraz Beko posiadają najwyższe oceny, a firmy Samsung oraz Dyson najniższe. Można więc dopatrzyć się tutaj ewidentnej korelacji w związku z ilością odkurzaczy sprzedanych przez daną firmę w Wielkopolskich placówkach rozważanej sieci sklepów.

#### **Wnioski**
Ćwicznie pozwoliło za utrwalenie umiejętności związanych się z Tier Protocol 3.0 oraz zasadami Tidy data, a także pozwoliło stworzyć prostą analizę danego zbioru danych w oparciu o bibliotekę matplotlib oraz pandas. Wnioski z analizy danych zostały przedstawione pod każdym wykresem.
