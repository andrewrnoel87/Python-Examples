import asyncio

async def print_values(values, delay):
    for item in values:
        print(item)
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(print_values([1, 3, 5], 0.2))
    task2 = asyncio.create_task(print_values([2, 4], 0.3))

    await task1
    await task2

asyncio.run(main())