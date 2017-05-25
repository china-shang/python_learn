#/usr/bin/env python
# coding=utf-8
import asyncio
import aiomysql
loop=asyncio.get_event_loop()
pool=2
async def creat_pool(loop):
    global pool
    pool=await aiomysql.create_pool(
        host='127.0.0.1',port=3306,
        password='',user='root',
        db='base1',loop=loop) 
async def select():
    global pool
    print("now select")
    print(pool)
    async with pool.get() as con:
            print("start")
            await cur.execute("select * FROM table1;")
            #await cur.commit()
            int
            #print(cur.description)
            r=await cur.fetchall()
            print(r)
    return r
try:
    loop.run_until_complete(creat_pool(loop))
    loop.run_until_complete(select())
    loop.run_forever()
except Exception as e:
    print(e)
finally:
    print("end")
