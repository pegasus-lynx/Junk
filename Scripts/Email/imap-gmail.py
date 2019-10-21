import sys
import imaplib
import email
from email import message as Msg
import datetime
import pprint as pp
import csv

# def getEmail(con):

# def getSubject(con):

# def getBody(con):

def process_request(con):
    con.utf8_enabled
    typ, data = con.search(None,'(SUBJECT "You have paid")')
    
    if typ=='OK':
        # print(data)
        pass
    else:
        print('Could not find any messages')
        sys.exit(6)

    # f = open('list.txt','w')

    with open('eggs.csv','w', newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for num in data[0].split():
            rv, mail = con.fetch(num, '(RFC822)')
            if rv != 'OK':
                print("Error getting mail:",num)
                continue
            msg = email.message_from_string(mail[0][1].decode())
            write.writerow(msg['From'].split()+[msg['Subject']])

            
            # print(msg.keys())

            # print(msg.get('Subject'))
            # print(msg.get('Received'))
            # keys = msg.keys()

            # for x in keys:
            #     print(x,msg.get(x))


print("Making Connection...")

try:
    con = imaplib.IMAP4_SSL('imap.gmail.com')
except:
    print('Connection Could not be established.')
    sys.exit(1)

try:
    con.login('dipeshkr.14@gmail.com','jcnurmgeuysongss')
except imaplib.IMAP4.error as e:
    print("Login Failed")
    sys.exit(2)

print('Logged In!')

print('Fetching Mailboxes...')
try:
    typ ,mailbox = con.list()
    print(type(mailbox))
    folders = [ x.decode() for x in mailbox ]
    print("OK")
    print("Mailboxes:\n")
    # print(*folders,sep='\n')
except:
    print('Error in fetching the list of mail boxes')
    sys.exit(3)

try:
    typ, folder = con.select('INBOX')
except:
    print('Could not fetch the given Mailbox.')
    sys.exit(4)

process_request(con)

# try:
    
# except:
#     print('Could not fetch the data required.')
#     sys.exit(5)

# Implement this part later. This part is to generalize the script basically for general purpose use.
# # The input command structure for 


# while True:
#     # Selecting the mail box:
