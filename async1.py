#!/usr/bin/env python
# coding=utf-8
import asyncio

async def hello():
    print("this cout")
    await asyncio.sleep(0.5)
async def input1():
    await asyncio.sleep(1)
    a=input("put \n")
    return a
async def server():
    cout=0
    while True:
        a=await input1()
        cout=cout+1
        if a=="exit":
            loop.stop()
            return
        await hello()
        print(a,"cout=",cout,'\n')
loop=asyncio.get_event_loop()
help(asyncio)
future=loop.create_future()
future.add_done_callback(hello)
#loop.run_until_complete(asyncio.wait([hello(),hello(),hello(),hello()]))
loop.run_until_complete(server())
loop.run_forever()
import os
def sleep():
    i=99999999
    while i>0:
        i=i-1
def hello():
    sleep()
    print("this cout")
def input1():
    sleep()
    a=input("put \n")
    return a
def server():
    cout=0

    while True:
        a=input1()
        cout=cout+1
        if a=="exit":
            return
        hello()
        print(a,"cout=",cout,'\n')
#server()
