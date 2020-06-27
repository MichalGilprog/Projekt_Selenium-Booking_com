# PROJEKT: AUTOMATYZACJA TESTÓW APLIKACJI WEBOWEJ W PYTHONIE

## Adres strony internetowej: Booking.com


[x] Zastosowanie wzorca Page Object 
[x] Zastosowanie Randrange from Random
[x] Zastosowanie DateTime

Autor/Autorzy:
Michał Gil


    1. Opis projektu

	Przykład: Celem projektu jest przetestowanie obszaru wyszukiwania hoteli/pensjonatów dla Booking.com. W tym celu opracowano opracowano przypadki testowe dla aktualizowanego czasu pobyto oraz losowo wybieranego wieku dzieci.

	W niniejszej pracy zastosowano wzorzec projektowy Page Object oraz testowanie z losowymi danymi.
Testowanie odbywa się przy zastosowaniu frameworków:
 Pytest do uruchamiania testów automatycznych 
oraz 
Allure które służy do tworzenia raportów z testów automatycznych.

    2. Przypadki testowe
Scenariusz testowy: Wyszukanie pensjonatów/hoteli na stronie Booking.com
    1) Odrzucenie zgody na wyświetlanie plików cookies
    2) Zmiana języka strony z polskiego na angielski
    3) Wprowadzenie nazwy miasta „Hel”
    4) Ustawienie daty zameldowania i wymeldowania  przy użyciu – datetime
    5) Wybór ilości dorosłych, dzieci i wieku dzieci - random
    6) Uruchomienie Wyszukiwania noclegów
    7) Pobieramy ilość pensjonatów wyświetlanych na stronie, sprawdzamy to w asercji – test drugi jest błędy z uwagi na wskazaną  niewłaściwą liczbę
    8) Wyświetlamy w jakiej walucie powinna być cena rezerwacji
    9) Sprawdzam czy kwota za wynajem jest podana we właściwej walucie 'zł'
    10) Wyświetlamy jaka jest liczba pensjonatów miejscowości która nas interesuje
    11) Sprawdzamy czy liczba pensjonatów z szukanej miejscowości jest zgodna z opisem
       
    3. Kod w Pythonie
	
		GITHUB
		
	(Załącznik do projektu stanowi film Booking_test.MP4)

    4. Wnioski (opcjonalne)
	Z uwagi na pozycjonowanie wyników wyszukiwania hoteli/pensjonatów wg. własnego algorytmu Booking.com otrzymane wyniki prawie zawsze są różne. 
	