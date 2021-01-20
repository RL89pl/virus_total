# Sprawdzanie, czy dany plik jest zainfekowany

### Zasady działania


**Ogólne zasady:** Skrypt sprawdza na platformie `virustotal.com`, czy plik umieszczony w folderze `danger_files` jest zainfekowany.
Dodatkowo tworzy plik `info.json` z pełnymi danymi.



### Przed uruchomieniem

**Wymagane pliki:** Przed uruchomieniem należy utworzyć plik "config.ini" i uzupełnić dane API:

```ini
[main]
API_KEY = <KLUCZ_API>

```
