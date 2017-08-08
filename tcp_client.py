#!/usr/bin/env python

# coding=utf-8

import socket
import time
import struct
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
print("client start")
#print (type(bytes))
# num=324
# sock.send(num.to_bytes(num.bit_length(),"little"))
s = [b'one', b'two', b'three', b'four', b'five', b'exit']

# print('rec',date.decode('utf-8'))
    #sock.send(struct.pack('d', date))
while True:
    sock.send(b'hello')
    date1 = sock.recv(1999)

    print( "recv:", date1)
