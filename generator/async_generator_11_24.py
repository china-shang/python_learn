#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

class Test:

    def __init__(self):
        self.count=3

    async def __anext__(self):

        self.count-=1
        if(self.count <=0 ):
            raise StopAsyncIteration
    
        for i in range(3):
            await self.__aiter_do__()

    def __aiter__(self):
        return self

    async def __aiter_do__(self):
        print("in aiter_do")

    async def __aenter__(self):
        print("in aenter")
        return "hello"

    async def __aexit__(self,exc_type,exc,tb):
        print("in aexit")


async def test():

    test=Test()

    async for i in test:
        print("in Block1")
    else:
        print("in Block2")

    for i in range(3):
        pass
    else:
        print("in Block2")


    async with test as t:
        print(t)


loop=asyncio.get_event_loop()
loop.run_until_complete(test())
