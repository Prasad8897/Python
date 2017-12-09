import sys
import smtplib
import time
import imaplib
import email
import time
from db_connection import *
reload(sys)
sys.setdefaultencoding('utf-8')

FROM_EMAIL  = "prasadc8897@gmail.com"
FROM_PWD    = "Pr@198897s@d"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def process1(msg,id):
    print ("\n\n\n\n\nNEW EMAIl")
    subject=msg['subject']
    print (subject)
    print (msg)

def process2(msg,id):
    print ("\n\n\n\n\nNEW EMAIL")
    data={}
    if msg['from']:
        data['from_email']=msg['from']
        print ("From:"+msg["from"])

    if msg['to']:
        data['to_email']=set_of_emails(msg['to'])
        print ("From:"+msg["from"])

    if msg['date']:
        data['date']=date_time_formating(msg['date'])
        print ("Date:"+msg["date"])

    if msg['from']:
        data['from_email']=msg['from']
        print ("From:"+msg["from"])

    if msg['from']:
        data['from_email']=msg['from']
        print ("From:"+msg["from"])
    if msg['from']:
        data['from_email']=msg['from']
        print ("From:"+msg["from"])
    
    
    if msg['to']: 
        print ("To:"+msg["to"])
    else:
        return
    if msg['subject']:
        print ("Subject:"+msg["subject"])
    else:
        return
    if msg["mailing-list"]:
        print ("Mailing-list:"+msg["mailing-list"])
        addToTable({'date':msg["date"],'from_email':msg["from"],'to_email':msg["to"],'mailing_list':msg["mailing-list"],'subject':msg["subject"],'id':id})


def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()   

    errors=[]
    
    for i in reversed(id_list):
            typ, data = mail.fetch(i, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode("utf-8",errors='ignore'))
                    try:
                        process2(msg,i)
                    except Exception as e:
                        dicts={}
                        dicts['id']=i
                        dicts['msg']=msg
                        dicts['error']=e
                        errors.append(dicts)

    for e in errors:
        print e

read_email_from_gmail()