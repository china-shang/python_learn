#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

loop = asyncio.get_event_loop()
async def f():
    return True
async def ff():
    if(await f()):
        print("True")
loop.run_until_complete(ff())


