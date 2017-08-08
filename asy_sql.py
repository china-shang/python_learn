# /usr/bin/env python
# coding=utf-8
import asyncio
import aiomysql
loop = asyncio.get_event_loop()
pool
help(aiomysql.Cursor)


async def creat_pool(loop):
    global pool
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, password='123456', user='root', db='test', loop=loop, charset='utf8', )


async def select():
    global pool
    print("now select")
    print(pool)
    async with pool.get() as con:
        async with con.cursor() as cur:
            print("start")
            await cur.execute("select * FROM books where name  = 'fji' ;")
            # await cur.commit()
            int
            # print(cur.description)
            r = await cur.fetchall()
            # print(r)
    return r
try:
    # asyncio.ensure_future(creat_pool(loop))
    # loop.run_until_complete(creat_pool(loop))
    # print(asyncio.ensure_future(select()))
    # print(loop.run_until_complete(select()))
    # loop.run_forever()

    async def sleep():
        await asyncio.sleep(3)
        print("sleep end")

    asyncio.ensure_future(sleep())
    asyncio.ensure_future(sleep())
    loop.run_forever()
    loop.run_until_complete(sleep())


except Exception as e:
    print('jjfisdjf\n\n')
    print(e)
finally:
    print("end")
