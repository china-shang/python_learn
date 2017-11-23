import asyncio

class Client:

    def __init__(self,reader,writer):
        self.reader=reader
        self.writer=writer

    async def handle(self):
        self.connect_lost=asyncio.Event()
        asyncio.ensure_future(self.handleReader())
        asyncio.ensure_future(self.handleWriter())

    async def handleReader(self):

        try:
            while True and not self.connect_lost.is_set() :
                s=await self.reader.readline()
                print(s.decode())
        except Exception as e:
            print(e)
            self.writer.close()
        finally:
            print("reader exit")

    async def handleWriter(self):

        data=["first\n","second\n","thrid\n","fourth\n","fifth\n","exit\n"]
        global flag
        try:
            for i in data:

                await asyncio.sleep(0.5)

                self.writer.write(i.encode("utf8"))
                print("writting",i)
                await self.writer.drain()

                if i=="exit\n":
                    
                    self.connect_lost.set()
                    self.writer.close()

        except Exception as e:
            print(e)
            self.writer.close()
        finally:
            print("writer exit")


async def tcp_echo_client():

    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    client=Client(reader,writer)
    await client.handle()
    await asyncio.sleep(100)


loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client())
loop.close()
