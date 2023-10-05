import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import smtplib
from email.mime.text import MIMEText
import config as conf

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg["From"] = conf.EMAIL_USERNAME
    msg["To"] = to
    msg["Subject"] = subject
    
    with smtplib.SMTP_SSL(conf.SMTP_SERVER, conf.SMTP_PORT) as server:
        server.login(conf.EMAIL_USERNAME, conf.EMAIL_PASSWORD)
        server.sendmail(conf.EMAIL_USERNAME, [to], msg.as_string())
