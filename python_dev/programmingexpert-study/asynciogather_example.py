import asyncio

async def print_values(values, delay):
    for item in values:
        print(item)
        await asyncio.sleep(delay)

    return delay

async def main():
    values = await asyncio.gather(print_values([1, 3, 5], 0.2), print_values([2, 4], 0.3))

    print(values)

asyncio.run(main())

# output:
#           1
#           2
#           3
#           4
#           5
#           [0.2, 0.3]