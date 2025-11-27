# Aplikacja do Parzenia Kawy (Coffee Brewing App)

Interaktywna aplikacja webowa stworzona w Django, pomagająca miłośnikom kawy zarządzać swoim ekwipunkiem oraz dobierać idealne przepisy parzenia.

## Funkcjonalności

*   **System Logowania**: Rejestracja i logowanie użytkowników.
*   **Zarządzanie Ekwipunkiem**:
    *   Dodawanie posiadanych zaparzaczy (np. V60, Chemex).
    *   Dodawanie posiadanych kaw (z informacjami o kraju, obróbce itp.).
    *   Podgląd "Mojego Ekwipunku".
*   **Dobieranie Przepisu**:
    *   System rekomendacji (obecnie w wersji podstawowej) dobierający przepis na podstawie posiadanego sprzętu.
    *   Wyświetlanie szczegółowych faz parzenia (Czynność, Czas, Ilość wody).
*   **Panel Administratora**:
    *   Możliwość dodawania nowych zaparzaczy, kaw oraz tworzenia złożonych przepisów z fazami.

## Instalacja i Uruchomienie

### Wymagania
*   Python 3.8+
*   pip

### Krok 1: Pobranie projektu i instalacja zależności

W katalogu głównym projektu uruchom:

```bash
pip install -r requirements.txt
```

### Krok 2: Przygotowanie bazy danych

Wykonaj migracje, aby utworzyć strukturę bazy danych (SQLite):

```bash
python manage.py migrate
```

### Krok 3: Utworzenie Administratora

Projekt posiada gotową komendę do utworzenia domyślnego administratora (login: `admin`, hasło: `adminpass`):

```bash
python manage.py create_initial_admin
```

Alternatywnie możesz utworzyć własnego superużytkownika:

```bash
python manage.py createsuperuser
```

### Krok 4: Uruchomienie serwera

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Instrukcja Obsługi

### Dla Użytkownika
1.  **Rejestracja/Logowanie**: Załóż konto lub zaloguj się.
2.  **Wybierz Zaparzacze**: Przejdź do zakładki "Wybierz Zaparzacze" i kliknij "Dodaj do ekwipunku" przy tych, które posiadasz.
3.  **Wybierz Kawy**: Podobnie dodaj kawy, które masz w domu.
4.  **Mój Ekwipunek**: Tutaj zobaczysz podsumowanie tego co masz.
5.  **Dobierz Przepis**: Kliknij "Znajdź idealny przepis", aby otrzymać instrukcję parzenia.

### Dla Administratora (Dodawanie Przepisów)
1.  Zaloguj się do panelu admina: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    *   Login: `admin` (lub Twój własny)
    *   Hasło: `adminpass` (lub Twoje własne)
2.  **Dodawanie Danych**:
    *   Dodaj **Zaparzacze** (Brewers) i **Kawy** (Coffees).
3.  **Tworzenie Przepisu**:
    *   Przejdź do **Przepisy** (Recipes) i kliknij "Add recipe".
    *   Wybierz Zaparzacz i Kawę.
    *   Ustal ilość kawy i stopień zmielenia.
    *   **Ważne**: Na dole strony w sekcji "Fazy parzenia" (Recipe phases) dodawaj kolejne kroki (np. Preinfuzja, Dolewanie), określając czas i ilość wody.
4.  Zapisz przepis. Od teraz będzie on dostępny dla użytkowników.
