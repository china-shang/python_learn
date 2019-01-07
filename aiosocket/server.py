#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import json
import struct
import time


class Handler(object):
    def __init__(self):
        pass

    async def call_back(self,
                        read:asyncio.StreamReader,
                        writer:asyncio.StreamWriter):

        while True:
            writer.write(b"hello world\n")
            await writer.drain()
            data=await read.readline()
            print(data.decode())
            time.sleep(3)






async def test():
    handler=Handler()
    host = "localhost"
    port=9999
    srv=await asyncio.start_server(handler.call_back, host=host, port=port)
    print(f"start server at {host}:{port}")

    await asyncio.sleep(1000)



if __name__ == "__main__":
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test())

