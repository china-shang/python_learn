#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def doNothing(future):
    future.set_result("sleep end")


async def sleep(timeout):
    f = asyncio.Future()
    loop.call_later(timeout, doNothing, f)
    print(await f)
    print(await testReturn())

async def testReturn():
    return "True"

async def test():
    await sleep(1)
    print("end")
    loop.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.run_forever()
