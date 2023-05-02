## Data appendix


"14_WIELKOPOLSKIE_final.csv":

Jest to zbiór danych po obróbce za pomocą skryptu "data_processing_script.ipynb".
Usunięte zostały w nim rekordy zawierające niepełną informację czyli:
- Rekordy pozbawione wieku osoby kupującej odkurzacz (wartość NaN).
- Rekordy nie zawierające informacji o płci ocoby kupującej odkurzacz (wartość bd.).

Poniżej przedstawiono opis każdej kolumny tabeli po obróbce znajdującej się w pliku 14_WIELKOPOLSKIE_final.csv:
- "Dni od zakupu" - Liczba dni pomiędzy datą zakupu odkurzacza przez klienta do czasu wystawienia przez niego oceny (int).
- "Marka" - Oficjalna nazwa producenta odkurzacza na którego zakup zdecydował się klient (string).
- "Wiek kupującego" - Wiek kupującego odkurzacz w latach (float).
- "Płeć kupującego" - Informacja o płci klienta ; M - mężczyzna; K - kobieta (string).
- "Ocena" - Ocena zakupionego przez klienta odkurzacza w skali od 0 do 5 z możliwym wystawianiem ocen połówkowych (float).
