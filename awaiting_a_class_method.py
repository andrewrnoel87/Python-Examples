import asyncio

class Test:
    @staticmethod
    async def test():
        print("hi")

async def main():
    await Test.test()

asyncio.run(main())