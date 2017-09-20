#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocess
from multiprocess import Process, Queue
import os


q = Queue()
def f(num):
    value = q.get()
    q.put(value+1)
    print(value)
    print("os.pid:", os.getpid(), num)
    return num * num


q.put(0)
plist = []
for i in range(8):
    plist.append(Process(target=f, args=(i, )))
    plist[i].start()
for i in plist:
    i.join()
