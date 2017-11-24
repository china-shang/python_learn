#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import ssl
import zlib
import struct
loop = asyncio.get_event_loop()


def deflate(data):
    return zlib.compress(data)[2:-4]


def inflate(data):
    return zlib.decompress(data, -zlib.MAX_WBITS)


async def get():
    # async with aiohttp.request("GET", "https://43.245.144.254/ncr",
    # connector = connect, headers = {'Host':'www.google.com'}) as rep:

    context = ssl.create_default_context()
    context.check_hostname = False

    kwargs = {}
    kwargs['password'] = "850747813"
    #kwargs['maxsize'] = config.AUTORANGE_MAXSIZE
    kwargs['timeout'] = '19'

    method = "GET"
    url = "http://www.baidu.com/"
    payload = '%s %s HTTP/1.1\r\n' % (method, url)
    #request_headers['Content-Length'] = str(len(body))

    payload += ''.join('X-URLFETCH-%s: %s\r\n' % (k, v)
                       for k, v in kwargs.items() if v)
    payload = payload.encode('utf8')
    payload = deflate(payload)
    print(len(payload))
    print(inflate(payload))
    body = struct.pack('!h', len(payload)) + payload + b''

    print(type(b'fji'))
    print(body)
    request_headers = {
        'Host': "my-project-1-1469878073076.appspot.com"
    }
    request_headers['Content-Length'] = str(len(body))
    async with aiohttp.ClientSession(conn_timeout=3,) as session:
        async with session.request("POST", "http://127.0.0.1:8080/_gh/", headers=request_headers, data=body) as resp:
            print(resp.headers)
            a = await resp.read()
            len1, = struct.unpack("!h", a[:2])
            print(len1)
            print((a[2 + len1:]))
            print(inflate(a[2:len1 + 2]))

loop.run_until_complete(get())
loop.run_forever()
