#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socks
import ssl
import http.client
import aiohttp
context = ssl.create_default_context()
context.check_hostname = False
import time
try:
    t = time.time()
    h1 = http.client.HTTPSConnection(
        "115.164.12.247",
        context=context,
        check_hostname=False)
    t1 = time.time()
    print((t1 - t) * 1000)
    h1.request("GET", "/_gh/", '',
               {'Host': "my-project-1-1469878073076.appspot.com"})
    r = h1.getresponse()
    print(r.status)
    print(r.getheaders())
except Exception as e:
    print(e)
finally:
    r.close()
