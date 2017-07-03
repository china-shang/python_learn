#!/usr/bin/env python
# coding=utf-8
import socket
import time
import threading


def rec(sock):
    date, adr = sock.recvfrom(1024)
    print('rec', date.decode('utf-8'))

    #//no join
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = [b'first', b'second', b'third']
t = threading.Thread(target=rec, args=(sock,))
t.start()
for date in s:
    time.sleep(2)
    sock.sendto(date, ('127.0.0.1', 8888))
    print('send', date.decode('utf-8'))
