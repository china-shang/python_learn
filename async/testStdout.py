#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys

def test(s,loop):
    data=sys.stdin.readline()

    print("input:",data)
    #loop.stop()

def run():
    try:

        print("start")
        loop=asyncio.get_event_loop()

        help(loop.add_reader)
        loop.add_reader(sys.stdin,test,sys.stdin,loop)
        loop.run_forever()
    except Exception as e:
        loop.stop()
        loop.close()
        print(e)


import select
import sys

async def do_nothing():
    pass

async def test_write_to_stdin():
    while True:
        await asyncio.sleep(0.3)
        print("test")

async def wait_can_read(fd,event):

    poll=select.poll()
    poll.register(fd,event)
    while True:
        t=poll.poll(1)
        if(len(t)==0):
            await asyncio.sleep(0.1)
        else:
            print("event:",t)
            print("input:"+fd.readline())


loop=asyncio.get_event_loop()
#loop.create_task(test_write_to_file(fd))
#loop.create_task(test_write_to_stdin())
loop.run_until_complete(wait_can_read(sys.stdin,select.POLLIN))


