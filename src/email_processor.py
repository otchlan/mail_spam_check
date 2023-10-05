import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess
import config as conf

def process_emails(emails):
    for email_msg in emails:
        # Tutaj można dodać kod do przetwarzania wiadomości e-mail
        # Na przykład, można zapisywać załączniki i uruchamiać skrypty przetwarzające
        # Wywołanie skryptu przetwarzającego
        subprocess.run([conf.PROCESSING_SCRIPT_PATH], shell=True)
