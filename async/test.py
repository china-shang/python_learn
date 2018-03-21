#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全双工通讯
import asyncio
import time
import struct

# +----+------+------+----------+----------+----------+
# |RSV | FRAG | ATYP | DST.ADDR | DST.PORT |   DATA   |
# +----+------+------+----------+----------+----------+
# | 2  |  1   |  1   | Variable |    2     | Variable |
# +----+------+------+----------+----------+----------+

# SOCKS5 UDP Response
# +----+------+------+----------+----------+----------+
# |RSV | FRAG | ATYP | DST.ADDR | DST.PORT |   DATA   |
# +----+------+------+----------+----------+----------+
# | 2  |  1   |  1   | Variable |    2     | Variable |
# +----+------+------+----------+----------+----------+

class Hander(object):

    TCP=1
    UDP=3

    def __init__(self,reader,writer,pool):

        super()
        self._is_running=True
        self._ver=0
        self._pool=pool
        
        self._cmd=None
        self._remote_reader=None
        self._remote_writer=None
        self._port=None
        self._address=""

        self._reader=reader
        self._writer=writer
        loop.create_task(self.init_sock())

    async def handle_connect(self):

        t=await self._reader.read(4)

        _,self._cmd,_,atyp=struct.unpack("!4b",t)

        if(atyp==1):
            t=await self._reader.read(4)
            ip=struct.unpack("!4B",t)
            for i in ip:
                self._address += str(i)
                self._address += "."
            self._address = self._address[:-1]

        if(atyp==3):
            t=await self._reader.read(1)
            n=struct.unpack("!b",t)[0]
            t=await self._reader.read(n)
            self._address=t.decode()

        if(atyp==4):
            t=await self._reader.read(16)
            print("ipv6")

        t=await self._reader.read(2)
        self._port=struct.unpack("!h",t)[0]
        print(self._address)
        print("port:",self._port)


        await self.connect_remote()

        loop.create_task(self.handle_client())
        loop.create_task(self.handle_server())

        if(self._cmd==Hander.TCP):
            self._writer.write(struct.pack("!4b4bh",5,0,0,1,0,0,0,0,0x1010));
        await self._writer.drain()

    async def connect_remote(self):
        try:
            self._remote_reader,self._remote_writer= await asyncio.open_connection(self._address,self._port)
            print("connect remote Sucess")
            print("writer:",self._remote_writer)
        except Exception as e:
            print(e)

    async def handle_client(self):
        print("handle_client")
        count=0
        while self._is_running:
            try:
                t=await self._reader.read(100)
                if(self._reader.at_eof()):
                    self.close()
                if(t!=b''):
                    print(t)
                    self._remote_writer.write(t)
                    await self._remote_writer.drain()
                    count=0
                else:
                    count += 1
                    if(count>5):
                        break
            except Exception as e:
                print(e)
                self.close()
        self.close()

    async def handle_server(self):
        print("handle_start")
        count=0
        while self._is_running:
            try:
                t=await self._remote_reader.read(100)
                if(self._reader.at_eof()):
                    self.close()
                print(t)
                if(t!=b''):
                    print(t)
                    self._writer.write(t)
                    await self._writer.drain()
                    count=0
                else:
                    count += 1
                    if(count>5):
                        break
            except Exception as e:
                print(e)
                self.close()
        self.close()

    def close(self):
        self._is_running=False
        self._remote_writer.close()
        self._writer.close()

    async def init_sock(self):

        t=await self._reader.read(1)
        self._ver=struct.unpack("!b",t)[0]
        print("version:",self._ver)

        t=await self._reader.read(1)
        n=struct.unpack("!b",t)[0]
        t=await self._reader.read(n)

        self._writer.write(struct.pack("!bb",5,0))
        await self._writer.drain()
        await self.handle_connect()

    async def handleWriter(writer):
        try:
            count=0

            while True:
                await asyncio.sleep(0.1)
                s=str(count)+":write\n"
                count+=1
                writer.write(s.encode("utf-8"))
                print("writting")
                await writer.drain()

        except Exception as e:
            print(e)
        finally:
            writer.close()

loop=asyncio.get_event_loop()
coro=asyncio.start_server(ConnectionCallBack,"127.0.0.1",8888,loop=loop)

asyncio.ensure_future(checkDeadConnection())
server=loop.run_until_complete(coro)

print("start server:",server.sockets[0].getsockname())
loop.run_forever()
loop.close()


