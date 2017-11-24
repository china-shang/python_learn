#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from aiohttp import web


async def handler(request):
    print(request)
    sock = request.transport.get_extra_info('socket')
    sock.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
    sock = None
    return b''


    #self.wfile.write(b'HTTP/1.1 200 OK\r\n\r\n')



async def main(loop):
    server = web.Server(handler)
    await loop.create_server(server, "127.0.0.1", 8080)
    print("======= Serving on http://127.0.0.1:8080/ ======")

    # pause here for very long time by serving HTTP requests and
    # waiting for keyboard interruption
    await asyncio.sleep(100*3600)


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
loop.close()

