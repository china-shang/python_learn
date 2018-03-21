# /usr/bin/env python
# coding=utf-8
import asyncio
import aiomysql
loop = asyncio.get_event_loop()


async def create_pool(loop):
    global pool
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, password='123456', user='root', db='database', loop=loop, charset='utf8', )
    print("end")


async def select():
    global pool
    print("now select")
    print(pool)
    async with pool.get() as con:
        async with con.cursor() as cur:
            print("start")
            await cur.execute("select * FROM teacher where 1=1 ;")
            # await cur.commit()
            # print(cur.description)
            r = await cur.fetchall()
            # print(r)
    pool.close()
    await pool.wait_closed()
    return r

f=asyncio.ensure_future(create_pool(loop))
loop.run_until_complete(f)
a=loop.run_until_complete(select())
print(a)
loop.close()
