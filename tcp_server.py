#!/usr/bin/env python
# coding=utf-8

import socket
import threading
import requests
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)


def server():
    ThreadList = []
    print("server start")
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


async def tcplink(sock_accept, addr):
    try:
        print("start\n")
        while True:
            date = sock_accept.recv(1024)
            if not date or date.decode('utf-8') == 'exit':
                break
            print(date)
            print("rec", date.decode('utf-8'))
        print(threading.current_thread().name, "end")
    except Exception as e:
        print(e)
        loop.stop()


async def server(sock):
    global loop
    print("server start at 8888")
    while True:
        sock_accept, addr = loop.sock_accept(sock)
        sock_accept.send(b'hello')

        await tcplink(sock_accept, addr)
loop = asyncio.get_event_loop()
loop.run_until_complete(server(sock))
loop.run_forever()


# if __name__=="__main__":
# try:
# server()
# except:
# print("exit")
# loop=asyncio.get_event_loop()
# import struct
# i=struct.pack('hhl',2,2,2)
