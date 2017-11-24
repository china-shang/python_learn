#!/usr/bin/env python
# coding=utf-8
import asyncio


async def Headle(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            return
        print(data)
        writer.write(data)
        await writer.drain()
loop = asyncio.get_event_loop()
coro = asyncio.start_server(Headle, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(coro)
loop.run_forever()
