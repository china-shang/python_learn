#!/usr/bin/env python
# coding=utf-8
def consumer():
    r = ''
    try:
        while True:
            try:
                n = yield r
            except Exception as e:
                print(e)
            if not n:
                print("not n")
                return
            print('[CONSUMER] Consuming %s...' % n)
            r = '200 OK'
    finally:
        print("closing")

def produce(c):
    print(next(c))
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
import asyncio

async def fun():
    i=await asyncio.sleep(1)

loop=asyncio.get_event_loop()
loop=loop.run_until_complete(fun())

