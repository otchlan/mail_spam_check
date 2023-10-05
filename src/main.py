import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from email_fetcher import fetch_emails
from email_processor import process_emails
from email_sender import send_email
import config as conf  # Poprawienie importu configu

def main():
    # Fetch Emails
    emails = fetch_emails()

    # Process Emails
    process_emails(emails)

    # Example to send an email (adjust as needed)
    send_email("to@example.com", "Subject", "Email body")

if __name__ == "__main__":
    main()

