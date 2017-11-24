#!/usr/bin/env python
# coding=utf-8
import asyncio


async def sleep(timeout):
    loop.call_later(timeout, fn)
    return


def fn():
    pass


async def Print(future):
    await sleep(1090)
    future.set_result("jfi")
    print("hello")


async def test(future):
    print("future.result = ", future.result())


future = asyncio.Future()
loop = asyncio.get_event_loop()
asyncio.ensure_future(Print(future))
task = asyncio.ensure_future(test(future))

loop.run_until_complete(task)
loop.run_forever()
