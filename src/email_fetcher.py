import imaplib
import email
from email import policy
import os
import config as conf
from utils.helpers import save_attachment  

def fetch_emails():
    mail = imaplib.IMAP4_SSL(conf.IMAP_SERVER, conf.IMAP_PORT)
    mail.login(conf.EMAIL_USERNAME, conf.EMAIL_PASSWORD)
    
    mail.select('inbox')
    
    status, messages = mail.search(None, "ALL")
    
    emails = []
    
    for message_id in messages[0].split():
        _, msg = mail.fetch(message_id, '(RFC822)')
        for response_part in msg:
            if isinstance(response_part, tuple):
                email_message = email.message_from_bytes(response_part[1], policy=policy.default)
                emails.append(email_message)
                
                save_attachment(email_message, conf.ATTACHMENT_DIR)
    
    mail.logout()
    return emails
