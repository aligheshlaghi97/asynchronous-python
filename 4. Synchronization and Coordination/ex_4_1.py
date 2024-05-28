import asyncio


async def task():
    global value
    tmp = value
    await asyncio.sleep(0.01)
    tmp = tmp + 1
    await asyncio.sleep(0.01)
    value = tmp


async def main():
    global value
    value = 0
    coroutines = [task() for _ in range(10000)]
    await asyncio.gather(*coroutines)
    print(value)

asyncio.run(main())
