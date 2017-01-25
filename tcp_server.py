#!/usr/bin/env python
# coding=utf-8

import socket
import threading
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8888))
sock.listen(4)

def server():
    print("server start")
    while True:
        sock_accept,addr=sock.accept()
        t=threading.Thread(target=tcplink,args=(sock_accept,addr))
        t.start()

def tcplink(sock_accept,addr):
    try:

        sock_accept.send(b'hello')

        print(threading.current_thread().name,"start")
        while True:
            date=sock_accept.recv(1024)
            if not date or date.decode('utf-8')=='exit':
                break
            print(date)
            print("rec",date.decode('utf-8'))
        print(threading.current_thread().name,"end")
    except:
        print("error")
    
server()


