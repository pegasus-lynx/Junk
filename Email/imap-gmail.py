import sys
import imaplib
import getpass
import email
import datetime
import pprint as pp

# def getEmail(con):

# def getSubject(con):

# def getBody(con):

def process_request(con):
    con.utf8_enabled
    typ, data = con.search(None,'ALL')
    
    if typ=='OK':
        print(data)
    else:
        print('Could not find any messages')
        sys.exit(6)


print("Making Connection...")

try:
    con = imaplib.IMAP4_SSL('imap.gmail.com')
except:
    print('Connection Could not be established.')
    sys.exit(1)

# print(type(con))

try:
    con.login('dipeshkr.14@gmail.com','jcnurmgeuysongss')
except imaplib.IMAP4.error as e:
    print("Login Failed")
    sys.exit(2)

print('Logged In!')

print('Fetching Mailboxes...')
try:
    typ,mailbox = con.list()
    print(type(mailbox))
    folders = [ x.decode() for x in mailbox ]
    print("OK")
    print("Mailboxes:\n")
    print(*folders,sep='\n')
except:
    print('Error in fetching the list of mail boxes')
    sys.exit(3)

try:
    rv, folder = con.select('[Gmail]/Drafts')
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
