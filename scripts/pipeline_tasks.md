# GitHub Activity Pipeline — 80 zadań

Plan nauki do rozmowy technicznej. Zadania 1–72 tworzą kompletny projekt: GH Archive → S3 → Python → PostgreSQL, sterowany jednym DAG-iem Airflow i uruchamiany w Dockerze na Linuxie. Zadania 73–80 są opcjonalnym rozszerzeniem.

## Jak korzystać

- Rób jedno zadanie naraz i przechodź dalej po spełnieniu warunku ukończenia.
- Pierwsze próby wykonuj na jednej stałej godzinie UTC. Większy zakres pojawia się dopiero pod koniec.
- Po etapie 16 kolejne etapy rozwijaj na branchach, zapisuj małe commity i scalaj przez pull requesty.
- Logika transformacji pozostaje poza DAG-iem. Airflow uruchamia istniejący kod.
- Mierz liczbę zdarzeń widocznych w archiwum; nie traktuj jej jako gwarantowanego pełnego obrazu aktywności GitHuba.
- Przy zmianie nazwy repozytorium lub loginu zdefiniuj spójną regułę aktualizacji. Uwzględnij, że starszy backfill nie powinien przypadkiem nadpisywać nowszej obserwacji.
- Zadania opisują cele i warunki ukończenia. Nie zawierają kodu ani gotowych konfiguracji.

## Prompt do pojedynczego zadania

„Robię GitHub Activity Pipeline. Jestem przy zadaniu [numer]: [treść]. Moje środowisko: [opis]. Dotychczas zrobiłem: [opis]. Pomóż mi wykonać tylko to zadanie. Wyjaśnij cel i potrzebne pojęcia, zadaj pytania naprowadzające, a potem daj jedną małą podpowiedź. Bez gotowego kodu i bez przechodzenia do kolejnych zadań. Na końcu pomóż mi sprawdzić warunek ukończenia.”

## Źródła

- [GH Archive — dane i nazewnictwo archiwów](https://www.gharchive.org/)
- [GitHub — typy i pola zdarzeń](https://docs.github.com/en/rest/using-the-rest-api/github-event-types)
- [Airflow — dobre praktyki](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [Airflow — uruchamianie zadań w Kubernetes](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html)
- [Spark — integracja z magazynami chmurowymi](https://spark.apache.org/docs/latest/cloud-integration.html)

## 1–8: Pozyskanie i obejrzenie danych

- [ ] **01. Poznaj GH Archive** — Otwórz stronę źródła i opisz, co reprezentuje pojedyncze zdarzenie.
  
  Gotowe, gdy: Potrafisz wyjaśnić źródło i zakres danych w dwóch zdaniach.

- [ ] **02. Wybierz godzinę** — Wybierz jedną zakończoną godzinę UTC z przeszłości i zapisz ją w notatkach.
  
  Gotowe, gdy: Masz jeden stały zakres do wszystkich początkowych prób.

- [ ] **03. Znajdź archiwum** — Znajdź adres pliku odpowiadającego wybranej godzinie.
  
  Gotowe, gdy: Rozumiesz związek między datą, godziną i nazwą pliku.

- [ ] **04. Pobierz dane ręcznie** — Pobierz ten jeden plik do lokalnego folderu roboczego.
  
  Gotowe, gdy: Masz zapisane archiwum oraz jego adres źródłowy.

- [ ] **05. Sprawdź plik** — Sprawdź rozmiar oraz możliwość poprawnego odczytania archiwum gzip.
  
  Gotowe, gdy: Potrafisz potwierdzić, że pobranie się udało.

- [ ] **06. Przygotuj próbkę** — Zapisz osobno około 30 rekordów; zachowaj oryginalne archiwum.
  
  Gotowe, gdy: Masz mały plik do wygodnego przeglądania.

- [ ] **07. Porównaj zdarzenia** — Obejrzyj trzy rodzaje zdarzeń; w razie potrzeby powiększ próbkę.
  
  Gotowe, gdy: Wskazujesz pola wspólne, zagnieżdżone i zależne od typu.

- [ ] **08. Zapisz obserwacje** — Zanotuj format rekordów, przykłady identyfikatorów i znaczniki czasu.
  
  Gotowe, gdy: Masz krótką notatkę z rozpoznania danych.

## 9–16: Środowisko, Linux i Git

- [ ] **09. Przygotuj Linux** — Wybierz jedno środowisko: Ubuntu w WSL2 albo posiadany Linux.
  
  Gotowe, gdy: Otwierasz terminal i odnajdujesz folder z danymi.

- [ ] **10. Uporządkuj projekt** — Ustal miejsca na kod, testy, dokumentację i lokalne dane.
  
  Gotowe, gdy: Każdy rodzaj pliku ma swoje miejsce.

- [ ] **11. Przygotuj Pythona** — Utwórz izolowane środowisko i sposób zapisywania zależności.
  
  Gotowe, gdy: Potrafisz odtworzyć środowisko z listy zależności.

- [ ] **12. Zainicjalizuj Git** — Utwórz lokalne repozytorium.
  
  Gotowe, gdy: Potrafisz sprawdzić jego stan i zmienione pliki.

- [ ] **13. Ustaw wykluczenia** — Wyklucz surowe dane, środowisko, pliki tymczasowe i sekrety.
  
  Gotowe, gdy: Przed pierwszym commitem sprawdzasz, co trafi do repozytorium.

- [ ] **14. Zrób pierwszy commit** — Zapisz szkielet projektu i krótki opis jego celu.
  
  Gotowe, gdy: Historia zawiera czytelny pierwszy commit.

- [ ] **15. Podłącz GitHub** — Utwórz zdalne repozytorium i wypchnij pierwszy commit.
  
  Gotowe, gdy: Widzisz swój projekt na GitHubie.

- [ ] **16. Otwórz branch** — Utwórz branch do napisania modułu pobierania.
  
  Gotowe, gdy: Prace nad pobieraniem prowadzisz na osobnej gałęzi.

## 17–24: Pobieranie danych Pythonem

- [ ] **17. Przyjmuj godzinę** — Zaprojektuj uruchomienie programu dla daty i godziny UTC podanych przez użytkownika.
  
  Gotowe, gdy: Zmiana godziny nie wymaga edytowania kodu.

- [ ] **18. Wyznacz adres i ścieżkę** — Na podstawie argumentów wyznacz adres źródła i lokalny plik docelowy.
  
  Gotowe, gdy: Dwie godziny wskazują dwa różne pliki.

- [ ] **19. Pobieraj porcjami** — Dodaj pobieranie HTTP zapisujące dane stopniowo na dysku.
  
  Gotowe, gdy: Program nie przechowuje całego pobranego pliku w RAM.

- [ ] **20. Obsłuż błędy HTTP** — Dodaj ograniczenie czasu oczekiwania i rozpoznawanie nieudanych odpowiedzi.
  
  Gotowe, gdy: Brak pliku lub timeout kończy się zrozumiałym błędem.

- [ ] **21. Obsłuż przerwanie** — Ustal zachowanie po zerwaniu pobierania w połowie.
  
  Gotowe, gdy: Niekompletny plik nie zostaje uznany za gotowe archiwum.

- [ ] **22. Obsłuż istniejący plik** — Ustal zasady ponownego pobrania tej samej godziny.
  
  Gotowe, gdy: Program odróżnia gotowy plik od niedokończonego.

- [ ] **23. Dodaj logowanie** — Zapisuj godzinę źródłową, rezultat, liczbę bajtów i czas pobierania.
  
  Gotowe, gdy: Z logów rozumiesz przebieg pojedynczego uruchomienia.

- [ ] **24. Zweryfikuj i scal** — Porównaj wynik z pobraniem ręcznym, sprawdź drugą godzinę i zamknij zmianę przez PR.
  
  Gotowe, gdy: Moduł działa dla dwóch godzin i ma czytelną historię zmian.

## 25–32: Parsowanie i projekt modelu

- [ ] **25. Czytaj stopniowo** — Przygotuj odczyt kolejnych rekordów z archiwum.
  
  Gotowe, gdy: Pierwsze rekordy przetwarzasz przed odczytaniem końca pliku.

- [ ] **26. Wybierz potrzebne pola** — Wskaż pola potrzebne do analizy zdarzeń, repozytoriów i użytkowników.
  
  Gotowe, gdy: Masz uzasadnioną listę pól ze ścieżkami w JSON-ie.

- [ ] **27. Zaprojektuj trzy tabele** — Rozpisz fact_events, dim_repository i dim_actor: ziarno, kolumny, typy i klucze.
  
  Gotowe, gdy: Wyjaśniasz, co oznacza jeden wiersz każdej tabeli.

- [ ] **28. Napisz transformację rekordu** — Przekształcaj jedno zdarzenie do ustalonej płaskiej reprezentacji.
  
  Gotowe, gdy: Funkcja działa na pojedynczym rekordzie bez sieci i bazy.

- [ ] **29. Ustal obsługę braków** — Rozdziel pola wymagane i opcjonalne; ustal reakcję na nieznany typ zdarzenia.
  
  Gotowe, gdy: Każdy przypadek ma jednoznaczną regułę.

- [ ] **30. Waliduj i odrzucaj** — Sprawdzaj identyfikatory i daty; zapisuj odrzucenia wraz z powodem.
  
  Gotowe, gdy: Wadliwy rekord można odnaleźć i zrozumieć przyczynę odrzucenia.

- [ ] **31. Przetwarzaj partiami** — Grupuj poprawne rekordy w partie o ograniczonym rozmiarze.
  
  Gotowe, gdy: Nie gromadzisz wszystkich faktów ani wymiarów w rosnących listach.

- [ ] **32. Podsumuj godzinę** — Policz rekordy odczytane, poprawne i odrzucone; oddziel czas zdarzenia od godziny pliku.
  
  Gotowe, gdy: Liczba odczytanych równa się sumie poprawnych i odrzuconych.

## 33–40: PostgreSQL i pierwszy pełny przepływ

- [ ] **33. Uruchom PostgreSQL** — Zainstaluj Docker i uruchom PostgreSQL przez Compose z trwałym wolumenem.
  
  Gotowe, gdy: Łączysz się z bazą, a restart kontenera zachowuje dane.

- [ ] **34. Przygotuj bazę projektu** — Utwórz bazę i konto dla danych analitycznych.
  
  Gotowe, gdy: Aplikacja ma własne miejsce na trzy tabele.

- [ ] **35. Utwórz wymiary** — Przygotuj skrypt tworzący obie tabele wymiarów i ich klucze.
  
  Gotowe, gdy: Możesz odtworzyć strukturę wymiarów w pustej bazie.

- [ ] **36. Utwórz fakty** — Dodaj tabelę faktów z unikalnością zdarzenia i powiązaniami do wymiarów.
  
  Gotowe, gdy: Baza odrzuca duplikat klucza i niepoprawne powiązanie.

- [ ] **37. Podłącz Pythona** — Dodaj konfigurowalne połączenie z bazą.
  
  Gotowe, gdy: Dane dostępowe nie są zapisane w kodzie ani commitach.

- [ ] **38. Ładuj wymiary** — Dodaj zapis partii wymiarów oraz regułę aktualizacji nazw po ID.
  
  Gotowe, gdy: Powtórne spotkanie użytkownika lub repozytorium nie mnoży wymiarów.

- [ ] **39. Ładuj fakty** — Dodaj zapis faktów i granicę transakcji obejmującą powiązane zmiany jednej partii.
  
  Gotowe, gdy: Cała partia jest spójna, a istniejące zdarzenia nie są dublowane.

- [ ] **40. Połącz lokalny przepływ** — Uruchom pobranie, transformację i ładowanie z terminala dla jednej godziny.
  
  Gotowe, gdy: Trzy tabele zawierają dane po jednym wywołaniu programu.

## 41–48: Poprawność, awarie i wynik analizy

- [ ] **41. Przygotuj dane testowe** — Zbuduj mały zestaw przykładów: poprawny rekord, brak pola, wadliwa data, zły JSON i duplikat.
  
  Gotowe, gdy: Testy korzystają z małych, znanych przykładów.

- [ ] **42. Przetestuj transformację** — Sprawdź mapowanie pól oraz przyjęte reguły walidacji.
  
  Gotowe, gdy: Test wykrywa celowo wprowadzony błąd transformacji.

- [ ] **43. Przetestuj pobieranie** — Zasymuluj poprawną odpowiedź, timeout i brak pliku.
  
  Gotowe, gdy: Testy nie zależą od dostępności internetu.

- [ ] **44. Sprawdź powtórne ładowanie** — Załaduj ten sam zestaw dwukrotnie do testowej bazy.
  
  Gotowe, gdy: Zestaw faktów i liczba wymiarów nie rosną przy drugim przebiegu.

- [ ] **45. Sprawdź awarię transakcji** — Wywołaj błąd w środku partii, a następnie ponów ładowanie.
  
  Gotowe, gdy: Nie zostaje częściowa partia, a wznowienie prowadzi do poprawnego wyniku.

- [ ] **46. Dodaj kontrolę danych** — Sprawdź klucze, relacje i rozliczenie rekordów, uwzględniając istniejące zdarzenia.
  
  Gotowe, gdy: Raport odróżnia nowe zdarzenia, duplikaty i odrzucenia.

- [ ] **47. Napisz trzy analizy SQL** — Policz najaktywniejsze repozytoria, unikalnych użytkowników i zdarzenia według rodzaju.
  
  Gotowe, gdy: Potrafisz objaśnić wyniki oraz różnicę między pushem a commitem.

- [ ] **48. Zmierz zasoby** — W Linuxie zaobserwuj czas, RAM i rozmiar danych dla ustalonej godziny.
  
  Gotowe, gdy: Masz zapisany pierwszy pomiar z opisem, co dokładnie mierzono.

## 49–56: Przeniesienie surowych danych na S3

- [ ] **49. Przygotuj bucket** — Wybierz region AWS i utwórz prywatny bucket projektu.
  
  Gotowe, gdy: Znasz jego nazwę, region i przeznaczenie.

- [ ] **50. Skonfiguruj dostęp** — Przygotuj dostęp Pythona do bucketu bez umieszczania sekretów w repozytorium.
  
  Gotowe, gdy: Mała próba zapisu i odczytu działa z Twojego środowiska.

- [ ] **51. Ustal nazwy obiektów** — Zaprojektuj klucze S3 rozdzielające dane według godziny źródłowej UTC.
  
  Gotowe, gdy: Ta sama godzina zawsze wskazuje to samo miejsce.

- [ ] **52. Wysyłaj archiwum** — Dodaj zapis kompletnego surowego archiwum do S3.
  
  Gotowe, gdy: Obiekt w S3 odpowiada poprawnie pobranemu plikowi.

- [ ] **53. Czytaj dane z S3** — Podłącz odczyt archiwum z S3 do istniejącego przetwarzania partiami.
  
  Gotowe, gdy: Odczyt działa bez ładowania całego obiektu do RAM.

- [ ] **54. Podepnij ładowanie** — Przeprowadź transformację danych z S3 i zapisz je do bazy.
  
  Gotowe, gdy: Te same dane dają taki sam wynik jak lokalne wejście.

- [ ] **55. Sprawdź ponowienie** — Ponów pobranie i ładowanie dla godziny, która już istnieje.
  
  Gotowe, gdy: Nie tworzysz kolejnych kopii tej samej godziny ani dodatkowych faktów.

- [ ] **56. Uruchom przepływ z S3** — Połącz źródło, S3, transformację, bazę i kontrolę wyniku w uruchomienie z terminala.
  
  Gotowe, gdy: Program kończy się czytelnym raportem i właściwym statusem powodzenia lub błędu.

## 57–64: Airflow i jeden DAG

- [ ] **57. Przygotuj środowisko Airflow** — Dobierz zgodne wersje i obraz zawierający zależności Twojego modułu Pythona.
  
  Gotowe, gdy: Środowisko Airflow potrafi zaimportować i uruchomić Twój kod.

- [ ] **58. Uruchom Airflow lokalnie** — Dodaj Airflow do Compose z oddzielną bazą metadanych.
  
  Gotowe, gdy: Panel działa, a dane aplikacji pozostają w bazie analitycznej.

- [ ] **59. Zaprojektuj DAG** — Ustal trzy zadania, kolejność oraz wspólny parametr godziny; przekazuj ścieżki i liczniki.
  
  Gotowe, gdy: Masz jeden DAG z jednoznacznym zakresem i małymi komunikatami między zadaniami.

- [ ] **60. Podepnij pobieranie** — Zaimplementuj zadanie download_to_s3 wywołujące istniejący moduł.
  
  Gotowe, gdy: Zadanie zapisuje archiwum i wskazuje jego adres.

- [ ] **61. Podepnij transformację** — Zaimplementuj zadanie transform_and_load korzystające z wyniku pobierania.
  
  Gotowe, gdy: Dane z tego konkretnego archiwum trafiają do trzech tabel.

- [ ] **62. Podepnij kontrolę** — Zaimplementuj validate_and_report i określ warunki niepowodzenia.
  
  Gotowe, gdy: Błąd jakości zatrzymuje przebieg, a poprawny wynik daje raport.

- [ ] **63. Ustal harmonogram** — Powiąż przetwarzanie z godziną źródłową, przewidź opóźnienie archiwum i kontroluj nadrabianie historii.
  
  Gotowe, gdy: Ponowienie starego przebiegu nie wybiera bieżącej godziny.

- [ ] **64. Przećwicz retry** — Wywołaj awarię jednego zadania, usuń przyczynę i pozwól je ponowić.
  
  Gotowe, gdy: DAG kończy się poprawnie, bez zduplikowania danych.

## 65–72: CI, Linux w AWS i przygotowanie demonstracji

- [ ] **65. Dodaj CI** — Uruchamiaj testy oraz sprawdzenie budowania obrazu przy pull requestach.
  
  Gotowe, gdy: Celowo zepsuty test blokuje zielony wynik CI; zwykłe testy nie potrzebują AWS.

- [ ] **66. Przygotuj EC2** — Utwórz maszynę Ubuntu z rolą dostępu do bucketu; ustal dostęp administracyjny i do panelu.
  
  Gotowe, gdy: Masz środowisko z uprawnieniami potrzebnymi projektowi.

- [ ] **67. Połącz się przez SSH** — Sprawdź użytkownika, uprawnienia, procesy, RAM i wolne miejsce.
  
  Gotowe, gdy: Samodzielnie odnajdujesz podstawowe informacje o serwerze.

- [ ] **68. Przenieś projekt** — Zainstaluj potrzebne narzędzia, sklonuj repozytorium i ustaw konfigurację środowiska.
  
  Gotowe, gdy: Serwer ma kod i konfigurację potrzebne do uruchomienia kontenerów.

- [ ] **69. Uruchom kontenery** — Uruchom Compose na EC2 i sprawdź logi, dostęp do S3 oraz bazy.
  
  Gotowe, gdy: Jeden przebieg DAG-a działa na Linuxie w AWS.

- [ ] **70. Przetwórz dobę** — Uruchom kontrolowane przetwarzanie 24 wybranych godzin; obserwuj postęp i zasoby.
  
  Gotowe, gdy: Masz 24 rozliczone godziny i brak przypadkowo uruchomionego wielkiego zakresu.

- [ ] **71. Uzupełnij README** — Opisz źródło, model, uruchomienie, wyniki, obsługę awarii oraz zatrzymanie zasobów po ćwiczeniu.
  
  Gotowe, gdy: Potrafisz odtworzyć projekt według własnej instrukcji.

- [ ] **72. Przećwicz rozmowę** — Pokaż przebieg, tabele, analizę i ponowienie; wyjaśnij pięć najważniejszych decyzji.
  
  Gotowe, gdy: W kilka minut przedstawiasz działanie i odpowiadasz, co dzieje się po awarii.

## 73–80: Opcjonalnie — Spark i Kubernetes

- [ ] **73. Wybierz większą próbę** — Ustal większy zakres, limit zasobów i punkt odniesienia z pomiarów wersji podstawowej.
  
  Gotowe, gdy: Wiesz, co chcesz sprawdzić i kiedy zatrzymać eksperyment.

- [ ] **74. Uruchom Spark z S3** — Przygotuj kontener ze Sparkiem, zgodnymi zależnościami i dostępem do małej próbki w S3.
  
  Gotowe, gdy: Spark potrafi odczytać próbkę z bucketu.

- [ ] **75. Odtwórz transformację** — Zapisz w PySparku te same reguły pól, typów i odrzuceń.
  
  Gotowe, gdy: Mała próbka daje ten sam logiczny wynik co Python.

- [ ] **76. Zapisz trzy zbiory Parquet** — Zbuduj fakt i dwa wymiary dla jawnie wybranego zakresu; zapisz je jako jeden zestaw wynikowy na S3.
  
  Gotowe, gdy: Wynik ma trzy zbiory, poprawne klucze i jednoznacznie opisany zakres.

- [ ] **77. Sprawdź powtórzenie Sparka** — Przetwórz ponownie ten sam zakres i sprawdź wynik.
  
  Gotowe, gdy: Ponowienie nie dokłada zdublowanych faktów ani wymiarów.

- [ ] **78. Porównaj wydajność** — Zmierz równoważną pracę na tych samych danych; oddziel czas transformacji od różnic w zapisie.
  
  Gotowe, gdy: Potrafisz uczciwie objaśnić czas, RAM i narzut obu wersji.

- [ ] **79. Uruchom zadanie na Kubernetes** — Na małym lokalnym klastrze uruchom kontener z istniejącym skryptem, ustawiając zasoby.
  
  Gotowe, gdy: Odczytujesz logi poda i jego status zakończenia.

- [ ] **80. Połącz Airflow z Kubernetes** — Uruchom tę transformację z DAG-a przez KubernetesPodOperator.
  
  Gotowe, gdy: Airflow zleca zadanie w podzie i rozpoznaje jego sukces albo błąd.

## Pierwszy krok

Zacznij od zadania 1: wejdź na GH Archive i własnymi słowami opisz pojedynczy rekord, zakres dostępnych danych oraz sposób podziału archiwów. Pobieranie pliku jest zadaniem 4; pisanie modułu Pythona zaczyna się w zadaniu 17.

