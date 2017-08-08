#!/usr/bin/env python
# coding=utf-8

import asyncio


async def hello():
    await asyncio.sleep(1)
    return

loop = asyncio.get_event_loop()
#loop.run_until_complete(asyncio.wait([hello()]))
#loop.run_forever()

import datetime


async def data(loop):
    endtime = loop.time() + 2
    while True:
        if loop.time() >= endtime:
            break
        print(datetime.datetime.now())
        await asyncio.sleep(1)

# loop.run_until_complete(data(loop))


async def other(future):
    future.set_result("end")
    await asyncio.sleep(1)


future = asyncio.Future()


# future.add_done_callback(other(future))
# asyncio.ensure_future(other(future))
loop.run_until_complete(future)

asyncio.wait_for(future, None)

# it will continue run next code in wait time;
# int above func

loop.run_until_complete(asyncio.sleep(2))
print(future.result())

# task=asyncio.Task(data,loop)
# loop.run_until_complete(task)
loop.close()
