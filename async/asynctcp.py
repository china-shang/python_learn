#!/usr/bin/env python
# coding=utf-8
import asyncio


async def handle(reader, writer):
    while True:
        #data = await reader.read(100)
        try:
            data = await asyncio.wait_for(reader.read(100),1)
        except Exception as e:
            print(e)
            break
        if not data:
            break
        print(data)
        writer.write(data)
    await writer.drain()
    writer.close()
loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(coro)
loop.run_forever()
