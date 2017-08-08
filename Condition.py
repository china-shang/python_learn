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
                cv.notify()
                print("Producer:", cout)
            else:
                cv.notify()


def Custom():
    global cv
    global cout
    while True:
        with cv:
            while (cout < 1):
                cv.wait()
            cout = cout-1
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
                cv.notify()

            time.sleep(1)
def check():
    global cout
    if cout > 0:
        return True
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
            cout = cout-1
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
