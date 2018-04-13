#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import concurrent.futures
import threading

data=[
    1,
    2,
    3
]
def do(data):
    print("do",data)
    while True:
        print(threading.currentThread().getName())

async def test():

    loop=asyncio.get_event_loop()
    excutor=concurrent.futures.ThreadPoolExecutor(max_workers=5)
    tasks=[loop.run_in_executor(excutor,do,i) for i in data]

    await asyncio.gather(*tasks)

def test1():
    print("in test1")
    print(threading.currentThread().getName())

loop=asyncio.get_event_loop()

loop.run_until_complete(test())
a=loop.run_in_executor(None,test1)
print(a)

