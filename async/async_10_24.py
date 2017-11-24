#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def doNothing():
    pass


def add(a):
    while True:
        a=yield (a+1)
    

def dec(a):
    while True:
        a = yield a-1


a = 0


async def addRun():
    global a
    f = add(a)
    next(f)

    a=a+1
    while True:
        print("add a=",a)
        a = f.send(a);
        while a >= 10:
            await asyncio.sleep(0.2)

    
async def decrun():
    global a
    f=dec(a)
    next(f)
    a -= a
    while True:
        print("dec a=", a)
        a=f.send(a)
        while a < 1:
            await asyncio.sleep(0.3)


class metaclasstest(type):
    def __new__(cls, name, *bases, **attrs):

        print("in metaclasstest __new__")
        return super().__new__(cls, name, *bases, **attrs)


class testclass(dict,metaclass=metaclasstest):

    def __init__(self):
        print("in testclass __init__")


testclassobject=testclass()
testclassobject=testclass()

loop=asyncio.get_event_loop()
# loop.create_task(addRun())
# loop.create_task(decrun())
# loop.run_forever()
