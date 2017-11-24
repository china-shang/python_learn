#!/usr/bin/env python
# coding=utf-8
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))


def server():
    print("start UDP server\n")
    while True:
        date, adr = sock.recvfrom(1024)
        sock.sendto(b'rec%s' % date, adr)
        print('recv', date.decode('utf-8'))


if __name__ == '__main__':
    try:
        server()
    except BaseException:
        print("\nexit")
