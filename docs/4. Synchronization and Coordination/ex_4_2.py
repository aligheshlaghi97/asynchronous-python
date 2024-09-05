import asyncio


async def task(lock):
    async with lock:
        global value
        tmp = value
        await asyncio.sleep(0.00)
        tmp = tmp + 1
        await asyncio.sleep(0.00)
        value = tmp


async def main():
    global value
    value = 0
    lock = asyncio.Lock()
    coroutines = [task(lock) for _ in range(10000)]
    await asyncio.gather(*coroutines)
    print(value)

asyncio.run(main())
