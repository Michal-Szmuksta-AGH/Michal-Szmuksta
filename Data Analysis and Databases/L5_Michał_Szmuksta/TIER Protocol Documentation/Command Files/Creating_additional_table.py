import pandas as pd

# Manualne wpisanie brakujących danych
additional_data = [('Antigua & Barbuda', 'North America'),
                   ('Bosnia-Herzegovina', 'Europe'),
                   ('Burkina Faso', 'Africa'),
                   ('Cote d\'Ivoire', 'Africa'),
                   ('Cabo Verde', 'Africa'),
                   ('Cook Islands', 'Oceania'),
                   ('Czech Republic', 'Europe'),
                   ('North Korea', 'Asia'),
                   ('DR Congo', 'Africa'),
                   ('Myanmar', 'Asia'),
                   ('Niue', 'Oceania'),
                   ('South Korea', 'Asia'),
                   ('St. Kitts & Nevis', 'North America'),
                   ('St. Lucia', 'North America'),
                   ('St. Vincent & the Grenadines', 'North America'),
                   ('Sao Tome & Principe', 'Africa'),
                   ('Timor-Leste', 'Asia'),
                   ('Trinidad & Tobago', 'South America'),
                   ('USA', 'North America')]

# Stworzenie tabeli
Continents_updated = pd.DataFrame()

for country, continent in additional_data:
    Continents_updated = pd.concat(
        [Continents_updated, pd.DataFrame({'Continent': continent, 'Country': country}, index=[0])], ignore_index=True)

# Zapis do pliku
Continents_updated.to_csv("../Original Data/countries-continents_additional_data.csv", index=False)
