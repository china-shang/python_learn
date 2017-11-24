#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


class Server:
    def __init__(self, loop, queue):
        self.loop = loop
        self.queue = queue
        self.count = 0
        self.max = 1000
        self._running = False
        self.create = True

    def start(self):
        if(not self._running):
            self._running = True
            print("start server ")
            self.loop.create_task(self.run())
            print("create_task run")

    def stop(self):
        self._running = False

    #def needdo(self):
        #if(self.count + self.queue.qsize() < self.queue.maxsize):
            #return True
        #else:
            #return False

    async def run(self):
        while self._running:
            #if(self.needdo() and self.count < self.max):
            if(self.create):
                self.create = False
                self.count = self.count + 1
                print("create_task do at ", self.count)
                self.loop.create_task(self.do())
                await asyncio.sleep(0.4)
            end = time.time()
    async def needdo(self):

        print("start needdo")
        while True:
            start = time.time()
            print(start)
            await asyncio.sleep(0.5)
            end = time.time()
            print(end)
            time_s = end-start
            if(time_s > 0.01):
                print(time_s, "creat")
                self.create = False
            else:
                print(time_s, "No creat")
                self.create = True


    async def do(self):
        print("doing item ")
        await asyncio.sleep(1)
        #print("start put")
        #await self.queue.put("item")
        #print("end put")
        self.count = self.count - 1


async def Custom(queue):
    while True:
        await asyncio.sleep(0.5)
        #await queue.get()
        #print("get item")


loop = asyncio.get_event_loop()
queue = asyncio.Queue(200)
server = Server(loop, queue)
asyncio.ensure_future(server.needdo())
server.start()
#loop.run_until_complete(Custom(queue))
loop.run_forever()
