#!/usr/bin/env python
# coding=utf-8
import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8888))
def server():
    while True:
        date,adr=sock.recvfrom(1024)
        sock.sendto(b'rec%s' % date,adr)
        print('recv',date.decode('utf-8'))
server()

