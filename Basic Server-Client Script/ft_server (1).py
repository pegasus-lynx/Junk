#! /usr/bin/python3

import socket
import select
import sys

class FileTransferServer():

    def __init__(self,port):
        self.ftserv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ftserv.bind(('0.0.0.0',port))
        self.ftserv.listen(1)
        self.clientsock = None

    def run(self):
        self.acceptconnection()
        ac_request = True
        while ac_request:
            st = self.clientsock.recv(100)
            if st.lower() == 'a':
                f = open('a.png', 'rb')
            else:
                f = open('b.png', 'rb')
            
            imgdata = f.read()
            f.close()

            self.clientsock.send(imgdata)

            print("Do you want to accept more request from this client?(y/n)")
            ans = str(input())
            if ans[0].lower()=='n':
                ac_request = False
                self.clientsock.send(b'Terminating your connection...')
            else:
                self.clientsock.send(b'Waiting for other request...\n')
        self.clientsock.close()
        self.clientsock = None

    def close(self):
        slef.ftserv.close()

    def acceptconnection(self):
        newsock, (remhost, remport) = self.ftserv.accept()
        self.clientsock = newsock
        print( "Client {} {} connected".format(remhost,remport))
        newsock.send(b'Connected to FTServer\nChoose "A" or "B" to recieve the image.\nWaiting for response...\n')


myServer = FileTransferServer( 2222 )
# acc = True
# while acc:
#     myServer.run()
#     print("Do you want to accept another client?(y/n)")
#     ans = str(input())
#     if ans[0].lower() == 'n':
#         print('Closing Server...')
#         acc = False
myServer.run()
myServer.close()