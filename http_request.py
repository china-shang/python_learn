#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

import aiohttp
import asyncio
import ssl
import zlib
import struct


def deflate(data):
    return zlib.compress(data)[2:-4]


def inflate(data):
    return zlib.decompress(data, -zlib.MAX_WBITS)


kwargs = {}
kwargs['password'] = "850747813"
#kwargs['maxsize'] = config.AUTORANGE_MAXSIZE
kwargs['timeout'] = '19'

method = "GET"
url = "https://www.baidu.com"
payload = '%s %s HTTP/1.1\r\n' % (method, url)
#request_headers['Content-Length'] = str(len(body))

payload += ''.join('X-URLFETCH-%s: %s\r\n' % (k, v)
                   for k, v in kwargs.items() if v)
payload = payload.encode('utf8')
payload = deflate(payload)
body = struct.pack('!h', len(payload))+ payload + b'jdif'

print(body)
request_headers = {
    'Host': "my-project-1-1469878073076.appspot.com"
}
request_headers['Content-Length'] = str(len(body))
response = requests.post(
    'http://127.0.0.1:8080/_gh/',
    headers=request_headers,
    data=body,
    timeout=3)
print(response.text)
