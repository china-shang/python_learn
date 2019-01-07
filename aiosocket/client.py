#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import json
import struct
import time

async def tcp_echo_client(message, loop):
    host="54.250.173.187"
    port=1111
    reader, writer = await asyncio.open_connection(host, port=port,
                                                        loop=loop)

    while True:
        data=await reader.readline()
        print(data.decode())
        writer.write(b"hello world\n")
        await writer.drain()
        time.sleep(3)
        


message = 'Hello World!\n'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()


