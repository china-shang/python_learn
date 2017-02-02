#!/usr/bin/env python
# coding=utf-8
import asyncio
import aiomysql
loop=asyncio.get_event_loop()
async def creat_pool(loop):
    global pool
    pool=await aiomysql.create_pool(
        host='127.0.0.1',port=3306,
        password='',user='root',
        db='base1',loop=loop) 
async def select():
    global pool
    async with pool as con:
        async with con.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("selecT name FROM students")
            await cur.commit()
            #print(cur.description)
            r=await cur.fetchall()
    return r

loop.run_until_complete(creat_pool(loop))
