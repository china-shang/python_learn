#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import threading
import concurrent.futures 
import requests
from requests import get
from concurrent.futures import ThreadPoolExecutor

url = "https://gitee.com/"

lock = threading.Lock()
count = 0
all = 30

def do():
    global count, lock, all
    while True:
        with lock:
            if count >= all:
                return

        get(url)
        count  += 1
        print(f"count = {count} in {threading.currentThread().getName()}")


def run_in(num):
    executor = ThreadPoolExecutor(num)
    futs = [executor.submit(do) for i in range(num)]
    for fut in concurrent.futures.as_completed(futs):
        fut.result()

def test():
    global lock, count
    l = []
    for j in range(19, 20, 1):
        start_time = time.time()
        run_in(j)
        end_time = time.time()
        during = end_time - start_time
        print(f"speed time:{during}")
        with lock:
            l.append({j:during / count})
            count = 0
    else:
        print(l)

if __name__ == "__main__":
    test()





