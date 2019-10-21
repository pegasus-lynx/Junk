#! /usr/bin/python3

import socket
import sys

clsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct format: IP address, port number")
try:
    host_addr = str(sys.argv[1])
    host_port = int(sys.argv[2])
except IndexError:
    host_addr = '127.0.0.1'
    host_port = 2222

clsock.connect((host_addr,host_port))

s = clsock.recv(100)
print(s)

while True:
    print("Choice:")
    ans = input()
    clsock.send(ans.encode())
    if ans[0].lower() == 'a':
        f = open('imga.png', 'wb')
    else:
        f = open('imgb.png', 'wb')

    f.write(clsock.recv(10240))
    f.close()

    s = clsock.recv(100).decode()
    print(s)
    if s == b'Waiting for other request...\n':
        pass
    else:
        break

clsock.close()