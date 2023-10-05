import os
import email

def save_attachment(msg, output_folder):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename is not None:
            filepath = os.path.join(output_folder, filename)
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))
