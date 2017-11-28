import sys
import smtplib
import time
import imaplib
import email
import time

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "prasadc8897" + ORG_EMAIL
FROM_PWD    = "Pr@198897s@d"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()   
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    for i in reversed(id_list):
        typ, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode("utf-8"))
                email_subject = msg['subject']
                email_from = msg['from']
                print ("NEW EMAIl")
                if msg.is_multipart():
                	for payload in msg.get_payload():
                		print (payload)
                else:
                	print (msg.get_payload())
                time.sleep(1)

read_email_from_gmail()