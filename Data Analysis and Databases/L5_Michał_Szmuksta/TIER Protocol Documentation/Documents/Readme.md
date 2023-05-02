1. Zawartość projektu

Niniejszy projekt analizy danych podzielony jest na 4 foldery:
- ../Original Data - zawierające wszelkie dane użyte do projektu w formacje csv. W tym także folder ../Original Data/Metadata
zawierający kompleksowe informacje odnoście danych w folderze Original Data.
- ../Comand Files - zawierający skrypt służący do przetworzenia danych, skrypt do wegenerowania danych uzupełniających
oraz skrypt służący w celach analizy danych napisane w języku python. Skrypty do przetwarzania i analizy zostały napisane
przy użyciu interaktywnego notatnika Jupyter Notebook.
- ../Analysis Data - zawierający przetworzone dane w formacie csv.
- ../Documents - zawierający wygenerowane dokumenty za pomocą skryptu w formatach pdf, html oraz md w osobnym podfolderze
wraz z fotografiami stworzonych wykresów. Folder zawiera także plik Readme, który właśnie czytasz będący krótkim przewodnikiem
po projekcie.

2. Instrukcja replikacji

Tu znajdziesz instrukcje replikacji w celu powtórzenia przetwarzania i analizy danych projektowych:
- W celu uruchomienia skryptów niezbędne jest posiadanie IDE umożliwiającego interpretację języka python w wersji 3.10
(np. Pycharm, VS Code). Niezbędne jest także posiadanie zainstalowanych pakietów: jupyterlab, pandas, pandasql oraz matplotlib.
- Aby skrypty zadziałały poprawnie muszą znajdować się w folderze "Command Files" równolegle z pustym folderem "Analysis Data"
oraz folderem "Original Data" zawierającym dwa pliki danych w formacie csv: "drinks" oraz "countries-continents".
- Folderem roboczym będzie "Command Files" zawierający wszystkie trzy skrypty "Creating_additional_table.py",
"Data_processing_script.ipynb" oraz "Data_analysis_script.ipynb".
- W celu przeprowadzenia poprawnej replikacji skrypty muszą być uruchamiane w następującej kolejności:
	1) Creating_additional_table.py - tworzy plik "countries-continents_additional_data.csv" w folderze Original Data.
	2) Data_processing_script.ipynb - wykorzystuje utworzoną w poprzednim kroku tabelę oraz dwa pozostałe pliki danych znajdujące
	się w folderze Original Data oraz tworzy plik drinks_final.csv w folderze Analysis Data.
	3) Data_analysis_script.ipynb - wykorzystuje Analysis Data/drinks_final.csv w celu generacji tabel i wykresów niezbędnych
	do analizy.
	4) W celu generacji raportu końcowego można zapisać skrypt Data_analysis_script.ipynb w formacie odpowiadającym
	indywidualnym potrzebom użytkownika. 
