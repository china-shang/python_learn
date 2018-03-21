#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys

def test(s,loop):
    data=sys.stdin.readline()

    print("input:",data)
    #loop.stop()

try:

    print("start")
    loop=asyncio.get_event_loop()

    help(loop.add_reader)
    loop.add_reader(sys.stdin,test,sys.stdin,loop)
    loop.run_forever()
    loop.close()
except Exception as e:
    print(e)
