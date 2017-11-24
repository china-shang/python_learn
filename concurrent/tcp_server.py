#!/usr/bin/env python
# coding=utf-8

import socket
import threading
import multiprocessing
import requests
import asyncio
import async_timeout


port=8888
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', port))
sock.listen(5)


def server():
    ThreadList = []
    print("server start in port:",port)
    while True:
        sock_accept, addr = sock.accept()
        print(sock_accept)
        t = threading.Thread(target=tcplink, args=(sock_accept, addr))
        ThreadList.append(t)
        t.start()


def tcplink(sock_accept, addr):
    try:

        sock_accept.send(b"Start------------\n")
        print(threading.current_thread().name, "start")
        while True:

            date = sock_accept.recv(2048)

            print("send ",date,"\n")
            sock_accept.send(date)
            print(date.decode('utf-8'))

            if not date or date.decode('utf-8') == 'exit':
                sock_accept.close()
                break
            #sock_accept.close()
            #break
        print(threading.current_thread().name, "end")
    except BaseException:
        print("error")


if __name__ == "__main__":
    try:
        server()
    except BaseException:
        print("exit")
