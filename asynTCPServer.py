#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全双工通讯
import asyncio

async def handleReader(reader,writer):
    try:
        print("in reader")

        while True:
            await asyncio.sleep(0.3)
            s=await reader.readline()
            print("reading:",s.decode("utf8"))
            if(s==b"exit\n"):
                print("closing")
                writer.close()
                break

    except Exception as e:
        print(e)


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
        writer.close()

def ConnectionCallBack(reader,writer):

    asyncio.ensure_future(handleReader(reader,writer))
    asyncio.ensure_future(handleWriter(writer))

loop=asyncio.get_event_loop()
coro=asyncio.start_server(ConnectionCallBack,"127.0.0.1",8888,loop=loop)

server=loop.run_until_complete(coro)
print("start server:",server.sockets[0].getsockname())
loop.run_forever()
loop.close()


