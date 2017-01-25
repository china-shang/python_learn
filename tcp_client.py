#!/usr/bin/env python
# coding=utf-8

import socket
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8888))
print("client start")
#print (type(bytes))
#num=324
#sock.send(num.to_bytes(num.bit_length(),"little"))
s=[b'fjif',b'fjif',b'exit']
date=sock.recv(1024)
print('rec',date.decode('utf-8'))
for date in s:
    sock.send(date)
    time.sleep(10)
    print("send",date.decode('utf-8'))
