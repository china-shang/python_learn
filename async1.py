#!usr/bin/env python
# coding = utf-8
import asyncio


async def base(arg):
    if arg == 0:
        print("base:", arg)
        return True
    else:
        print("base:", arg)
        return False


async def hello():
    while True:
        for i in range(10, -1, -1):
            i = await base(i)
            if i is True:
                print("await base = ", i)
                return True


async def input1():
    print("input")


async def server():
    print("server start")
    cout = 0
    while cout < 3:
        print(" <<\n")
        a = await input1()
        cout = cout + 1
        print(a, "cout = ", cout, '\n')
        if a == "exit":
            loop.stop()
            return
        await hello()
        print(" >>\n")
    loop.stop()
loop = asyncio.get_event_loop()
# future = loop.create_future()
# future.add_done_callback(hello)
loop.run_until_complete(asyncio.wait
                        ([hello(), hello(), hello(), hello(), input1()]))
# asyncio.wait()是协程
# loop.run_until_complete(server())
loop.run_forever()
