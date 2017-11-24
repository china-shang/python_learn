#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import warnings
import aiohttp
import os
import ssl
import async_timeout
import time
import get_ip
warnings.simplefilter('ignore')


class Test_Ip:
    def __init__(self):
        #global f
        #self.f = f
        self.d = dict()
        print("start")
        self.ipcreator = get_ip.IpCreator()
        self.ipcreator.find_ip()
        self.generateIp = self.ipcreator.generate
        self.max = 64
        self.now = 0

    async def test(self, ip):
        start_time = time.time()
        #global connect
        # print(connect.limit)
        try:
            with async_timeout.timeout(2.5):
                async with aiohttp.request("GET", "https://%s/_gh/" % ip, headers={"Host": "my-project-1-1469878073076.appspot.com"}, connector=connect, loop=loop) as resp:
                    # async with aiohttp.request("GET", "http://%s/_gh/" % ip, headers={"Host": "my-project-1-1469878073076.appspot.com"}) as resp:
                    # print(resp.headers)
                    headers = resp.headers
                    server_type = headers.get('Server', '')
                    len = headers.get('Content-Length', '')
                    if int(len) == 86:
                        end_time = time.time()
                        time_used = end_time - start_time
                        #print(ip,"status:", resp.status ,"time_used:", time_used)
                        self.d[ip] = time_used
                        return True
                    if resp.status == 503:
                        # out of quota
                        if "gws" not in server_type and "Google Frontend" not in server_type and "GFE" not in server_type:
                            return False
                        else:
                            end_time = time.time()
                            time_used = end_time - start_time
                            #print(ip, "time_used:", time_used)
                            self.d[ip] = time_used
                            return True
                    else:
                        return False
        except Exception as e:
            pass
            # print(e)

    async def wait_for(self):
        try:
            ip = await self.generateIp()
            #print("test ip")
            if ip not in self.d:
                self.d[ip] = 0
            # await asyncio.wait([ self.test(ip), self.test(ip), self.test(ip)], timeout=3)
            # await asyncio.gather(( self.test(ip), self.test(ip),
            # self.test(ip)) )
            success = await self.test(ip)
            if success:
                print(ip, "Success time_used:", self.d[ip])
            else:
                if ip in self.d:
                    del self.d[ip]
                #print(ip, "failed")
        finally:
            self.now -= 1
            #print("Task Done :", self.now)
            self.now += 1
            ##print("start Task Sum: ", self.now)
            asyncio.ensure_future(self.wait_for())

    async def Server(self):
        create = True
        while True:
            if self.now < self.max and create:
                self.now += 1
                #print("start Task Sum: ", self.now)
                asyncio.ensure_future(self.wait_for())
            else:
                await asyncio.sleep(100)


                #start = time.time()
                # await asyncio.sleep(4.5)
                #end = time.time()
                #time_pro = (end-start-4.5)*1000
                #print("time:", time_pro, "count:", self.now)
                # if(time_pro < 1):
                    #self.max += 5
                # else:
                    #self.max -= 5
                #print("Task Sum:", self.now)
# os.fork()
# os.fork()
# os.fork()
loop = asyncio.get_event_loop()
testip = Test_Ip()
context = ssl.create_default_context()
context.check_hostname = False
connect = aiohttp.TCPConnector(
    ssl_context=context,
    force_close=True,
    limit=1000)
try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        loop.run_until_complete(testip.Server())
except Exception as e:
    print(e)
# finally:
    # loop.stop()
    # loop.close()
    # f.close()
# loop.run_until_complete(
    # asyncio.gather(
        # test("115.164.12.247"),
        # test("115.164.12.247"),
        # test("115.164.12.247"),
        # test("115.164.12.247")))
