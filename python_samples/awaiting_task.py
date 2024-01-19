import asyncio

async def print_something():
    await asyncio.sleep(1)
    print("something")
    return "finished"

async def main():
    print("main")

    task = asyncio.create_task(print_something())

    print("main again")
    result = await task
    print(result)

asyncio.run(main())