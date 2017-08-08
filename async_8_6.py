#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def doNothing(future):
    future.set_result("sleep end")


async def sleep(timeout):
    global loop
    f = asyncio.Future()
    loop.call_later(timeout, doNothing, f)
    await f
    

async def test():
    await sleep(1)
    print("end")


loop = asyncio.get_event_loop()
loop.run_until_complete(sleep(1))
loop.run_forever()
