#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全双工通讯
import asyncio
import time

async def handleReader(reader,writer):

    global pool
    def checkEnd(s,mime):
        if(s==b""):
            return True
        return False

    try:

        print("in reader")
        mime=False

        while True:

            #await asyncio.sleep(0.3)
            s=await reader.read(1000)
            print("reading:",s)
            pool[writer]=time.time()

            writer.write(s)
            await writer.drain()

            if(checkEnd(s,mime)):
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
    finally:
        writer.close()

async def ConnectionCallBack(reader,writer):

    global pool
    task=asyncio.ensure_future(handleReader(reader,writer))
    pool[writer]=time.time()

    #asyncio.ensure_future(handleWriter(writer))

async def checkDeadConnection():

    global pool
    while True:
        await asyncio.sleep(2)
        nowTimer=time.time()

        for i in list(pool):
            lastTime=pool[i]
            if(nowTimer-lastTime>3):
                i.close()
                pool.pop(i)
                print("DeadConnect ")

pool=dict()
loop=asyncio.get_event_loop()
coro=asyncio.start_server(ConnectionCallBack,"127.0.0.1",8889,loop=loop)

asyncio.ensure_future(checkDeadConnection())
server=loop.run_until_complete(coro)

print("start server:",server.sockets[0].getsockname())
loop.run_forever()
loop.close()


