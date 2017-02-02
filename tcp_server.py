#!/usr/bin/env python
# coding=utf-8

import socket
import threading
import requests
import asyncio
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8888))



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
        #print(threading.current_thread().name,"end")
    except:
        print("error")
async def tcplink(sock_accept,addr):
    try:
        print("start\n")
        while True:
            date=sock_accept.recv(1024)
            await asyncio.sleep(0.1)
            if not date or date.decode('utf-8')=='exit':
                break
            print(date)
            print("rec",date.decode('utf-8'))
        print(threading.current_thread().name,"end")
    except Exception as e:
        print(e)
        loop.stop()
async def server():
    print("server start")
    while True:
        sock_accept,addr=loop.sock_accept(sock)
        sock_accept.send(b'hello')

        await tcplink(sock_accept,addr)
    
loop=asyncio.get_event_loop()
help(loop.sock_accept)
loop.run_until_complete(server())
loop.run_forever()


#if __name__=="__main__":
    #server()

