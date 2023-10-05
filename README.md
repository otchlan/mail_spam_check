Utworzono strukturę folderów i plików projektu. Proszę teraz dostosować poszczególne pliki .py zgodnie z poniższymi wskazówkami:

src/email_fetcher.py: Kod, który jest odpowiedzialny za łączenie się ze skrzynką e-mail i pobieranie e-maili.

src/email_processor.py: Kod odpowiedzialny za przetwarzanie pobranych e-maili, w tym ekstrakcję i przetwarzanie załączników oraz zawartości e-maili.

src/email_sender.py: Kod odpowiedzialny za wysyłanie e-maili po przetworzeniu.

src/main.py: Główny plik, który orkiestruje działanie powyższych skryptów i funkcji.

utils/helpers.py: Dodatkowe funkcje pomocnicze, które mogą być używane w różnych miejscach projektu.

config/config.py: Konfiguracja, takie jak dane uwierzytelniające do konta e-mail, ścieżki do folderów itp.

scripts/run.sh: Skrypt shell do uruchamiania głównej funkcji projektu.

scripts/processing_script.sh: Skrypt, który przetwarza e-maile/załączniki zgodnie z Twoimi potrzebami.

tests/: Folder zawierający wszystkie Twoje testy jednostkowe i integracyjne dla różnych części projektu.

logs/: Folder, w którym będą przechowywane logi dotyczące przetwarzania e-maili.

attachments/: Folder, w którym będą przechowywane wszelkie załączniki z pobranych e-maili.

processed_attachments/: Folder, w którym będą przechowywane załączniki po przetworzeniu.

README.md: Dokumentacja Twojego projektu - jak go uruchomić, konfigurować itp.
