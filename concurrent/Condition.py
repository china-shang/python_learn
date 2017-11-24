#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import subprocess

#commmand = "ls   &&  sleep 2"
#import shlex

#args = commmand
# pip = subprocess.Popen(
    # args,
    # shell=True,
    # stdout=subprocess.PIPE)


#out, N = pip.communicate(timeout=3)
#print(out.decode().replace('\n', '\t'))


#import time
#import pprint

import threading
import time

cv = threading.Condition()
cout = 0


def Producer():
    global cv
    global cout
    while True:
        with cv:
            if(cout < 10):
                cout = cout + 1
                print("Producer:", cout)
            if(cout > 0):
                cv.notify()


def Custom():
    global cv
    global cout
    while True:
        with cv:
            while (cout < 1):
                print("waitting")
                cv.wait()
            cout = cout - 1
            print("Custom ", cout)


def Producer():
    global cv
    global cout
    while True:
        with cv:
            if(cout < 10):
                cout = cout + 1
                cv.notify(cout)
                print("Producer:", cout)
            else:
                cv.notify(cout)

            time.sleep(1)


def check():
    global cout
    print("check")
    if cout > 0:
        return True
    else:
        return False


def Custom():
    global cv
    global cout
    while True:
        with cv:
            print("start wait")
            cv.wait_for(check)
            print("end wait")
            time.sleep(1)
            cout = cout - 1
            print("Custom:", cout)


def main():
    threading.Thread(
        target=Custom
    ).start()
    threading.Thread(
        target=Custom
    ).start()
    threading.Thread(
        target=Producer
    ).start()

    try:
        time.sleep(100)
    except Exception as e:
        print(e)
main()

import asyncio

#q = asyncio.Queue()
#loop = asyncio.get_event_loop()

#async def Producer():
    #i = 0
    #while True:
        #i = (i+1)%10
        #if q.qsize() < 10:
            #await q.put(i)
        #await asyncio.sleep(0.3)
        #print("this  Producer:", q.qsize())

#async def Custom():
    #while True:
        #i = await q.get()
        #await asyncio.sleep(1)
        #print("this  Custom:", i)

#loop.create_task(Producer())
#loop.create_task(Custom())
#loop.run_forever()

