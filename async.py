#!/usr/bin/env python
# coding=utf-8

import asyncio


@asyncio.coroutine
def fun():
    print("the fun start")
    yield from fun1()
    # 遇到yield同时进行下一任务与yield后
    # from 后为coroutine对象
    print("end")


def fun1():
    print("the fun1 start")
    yield from asyncio.sleep(1)
    print("fun1 end")


loop = asyncio.get_event_loop()
task = [fun(), fun1(), fun()]
loop.run_until_complete(asyncio.wait(task))

print("all end")


async def new():
    print("python 3 new ")
    a = await asyncio.sleep(1)
    # 等后面函数同时执行其他任务
loop.run_until_complete(new())
