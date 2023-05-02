1. Zawartość projektu

Niniejszy projekt analizy danych podzielony jest na 4 foldery:
- ../Original Data - zawierające wszelkie dane użyte do projektu w formacje csv. W tym także folder ../Original Data/Metadata
zawierający kompleksowe informacje odnoście danych w folderze Original Data.
- ../Comand Files - zawierający skrypt służący do przetworzenia danych, oraz skrypt służący w celach analizy danych 
napisane w języku python. Obydwa skrypty zostały napisane przy użyciu interaktywnego notatnika Jupyter Notebook.
- ../Analysis Data - zawierający przetworzone dane w formacie csv.
- ../Documents - zawierający wygenerowane dokumenty za pomocą skryptu w formatach pdf, html oraz md w osobnym podfolderze
wraz z fotografiami stworzonych wykresów. Folder zawiera także plik Readme, który właśnie czytasz, będący krótkim przewodnikiem
po projekcie.

2. Instrukcja replikacji

Tu znajdziesz instrukcje replikacji w celu powtórzenia przetwarzania i analizy danych projektowych:
- W celu uruchomienia skryptów niezbędne jest posiadanie IDE umożliwiającego interpretację języka python w wersji 3.10
(np. Pycharm, VS Code). Niezbędne jest także posiadanie zainstalowanych pakietów: jupyterlab, pandas, numpy oraz matplotlib.
- Aby skrypty zadziałały poprawnie muszą znajdować się w folderze "Command Files" równolegle z pustym folderem "Analysis Data"
oraz folderem "Original Data" zawierającym plik danych w formacie csv: "14_WIELKOPOLSKIE.csv".
- Folderem roboczym będzie "Command Files" zawierający obydwa skrypty "data_processing_script.ipynb" oraz "data_analysis_script.ipynb".
- W celu przeprowadzenia poprawnej replikacji skrypty muszą być uruchamiane w następującej kolejności:
	1) Data_processing_script.ipynb - wykorzystuje plik danych "14_WIELKOPOLSKIE.csv" znajdujący się w folderze 
	Original Data oraz tworzy obrobiony plik "14_WIELKOPOLSKIE_final.csv" w folderze Analysis Data.
	2) Data_analysis_script.ipynb - wykorzystuje Analysis Data/14_WIELKOPOLSKIE_final.csv w celu generacji tabel, 
	wykresów i tekstu niezbędnego do analizy.
	3) W celu generacji raportu końcowego można zapisać skrypt Data_analysis_script.ipynb w formacie odpowiadającym
	indywidualnym potrzebom użytkownika. 
