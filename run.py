import os
import sys

# Dodaj ścieżki 'src' oraz 'config' do sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))

# Importuj główny skrypt
from main import main

# Uruchom główną funkcję
if __name__ == "__main__":
    main()
