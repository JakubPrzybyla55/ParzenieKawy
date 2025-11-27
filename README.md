# ParzenieKawy

Projekt aplikacji webowej do zarządzania parzeniem kawy, stworzony w oparciu o framework Django. Aplikacja pozwala użytkownikom na zarządzanie ekwipunkiem (młynki, ekspresy) oraz kawami.

## Wymagania

Aby uruchomić projekt, potrzebujesz zainstalowanych następujących narzędzi:

1.  **Python** (zalecana wersja 3.10 lub nowsza) - [Pobierz Python](https://www.python.org/downloads/)
2.  **Visual Studio Code** - [Pobierz VS Code](https://code.visualstudio.com/)

Zalecamy również zainstalowanie rozszerzenia **Python** dla VS Code (od Microsoft).

## Instalacja i Konfiguracja

Postępuj zgodnie z poniższymi krokami, aby skonfigurować środowisko deweloperskie.

### 1. Pobranie projektu

Sklonuj repozytorium lub pobierz pliki projektu do wybranego katalogu na swoim komputerze.

### 2. Utworzenie wirtualnego środowiska (Virtual Environment)

Otwórz terminal w VS Code (Terminal -> New Terminal) lub systemowy wiersz poleceń w katalogu projektu i wykonaj komendę:

**Windows:**
```bash
python -m venv venv
```

**macOS / Linux:**
```bash
python3 -m venv venv
```

### 3. Aktywacja środowiska

Przed instalacją bibliotek musisz aktywować utworzone środowisko.

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```
*Jeśli wystąpi błąd uprawnień, możesz potrzebować wykonać `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.*

**Windows (CMD):**
```bash
.\venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

Po poprawnej aktywacji, w terminalu powinieneś widzieć prefiks `(venv)`.

### 4. Instalacja zależności

Zainstaluj wymagane biblioteki (Django) za pomocą pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Konfiguracja Visual Studio Code

Projekt zawiera predefiniowaną konfigurację dla VS Code.

1.  Folder `.vscode` zawiera plik `launch.json`, który pozwala na uruchamianie i debugowanie serwera bezpośrednio z zakładki "Run and Debug" (Ctrl+Shift+D).
2.  Plik `settings.json` wskazuje VS Code, aby używał interpretera z wirtualnego środowiska `venv`.

Po otwarciu folderu projektu w VS Code, upewnij się, że wybrano odpowiedni interpreter (Prawy dolny róg -> wybierz `venv` lub użyj skrótu `Ctrl+Shift+P` -> `Python: Select Interpreter`).

## Baza Danych i Pierwsze Uruchomienie

### 1. Migracje bazy danych

Projekt korzysta z bazy SQLite. Aby utworzyć strukturę bazy danych, wykonaj:

```bash
python manage.py migrate
```

### 2. Utworzenie superużytkownika (Admina)

Projekt posiada dedykowaną komendę do utworzenia domyślnego konta administratora. Wykonaj:

```bash
python manage.py create_initial_admin
```
To polecenie utworzy użytkownika z uprawnieniami administratora.
**Domyślne dane logowania:**
*   **Login:** `admin`
*   **Hasło:** `adminpass`

### 3. Uruchomienie serwera

Możesz uruchomić serwer na dwa sposoby:

**Sposób A: Z terminala**
```bash
python manage.py runserver
```

**Sposób B: Przez VS Code (Debugowanie)**
Przejdź do zakładki "Run and Debug" po lewej stronie (ikona z robakiem i trójkątem) i kliknij zielony trójkąt obok "Python: Django".

Serwer powinien uruchomić się pod adresem: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Struktura Aplikacji

*   **coffee_project/**: Główne ustawienia projektu.
*   **brewing/**: Aplikacja zawierająca logikę biznesową (modele kaw, przepisy, widoki).
*   **manage.py**: Narzędzie do zarządzania projektami Django.

## Notatki

*   Aby zakończyć działanie serwera w terminalu, użyj skrótu `Ctrl+C`.
*   Aby wyjść z wirtualnego środowiska, wpisz komendę `deactivate`.
