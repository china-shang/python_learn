#!/usr/bin/env python
# coding=utf-8
import asyncio
import aiomysql
loop=asyncio.get_event_loop()
async def creat_pool(loop):
    async with aiomysql.create_pool(
        host='127.0.0.1',port=3306,
        password='',user='root',
        db='base1',loop=loop) as pool:
        async with pool.get() as con:
            async with con.cursor() as cur:
                await cur.execute("selecT name FROM students")
                #print(cur.description)
                r=await cur.fetchall()
                print(r)

loop.run_until_complete(creat_pool(loop))
