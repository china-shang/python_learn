#!/usr/bin/env python
# coding=utf-8

import socket
import threading
import multiprocessing
import requests
import asyncio
import async_timeout


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)


def server():
    ThreadList = []
    print("server start in port:8888")
    while True:
        sock_accept, addr = sock.accept()
        t = threading.Thread(target=tcplink, args=(sock_accept, addr))
        ThreadList.append(t)
        t.start()


def tcplink(sock_accept, addr):
    try:

        sock_accept.send(b'hello')

        print(threading.current_thread().name, "start")
        while True:
            date = sock_accept.recv(1024)
            if not date or date.decode('utf-8') == 'exit':
                print("recv exit")
                sock_accept.close()
                break
            print(date)
            print("rec", date.decode('utf-8'))
        print(threading.current_thread().name, "end")
    except BaseException:
        print("error")


if __name__ == "__main__":
    try:
        server()
    except BaseException:
        print("exit")
# loop=asyncio.get_event_loop()
# import struct
# i=struct.pack('hhl',2,2,2)
