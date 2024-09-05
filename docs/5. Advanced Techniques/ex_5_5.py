import asyncio


async def producer(channel: asyncio.Queue):
    for num in range(0, 5):
        await asyncio.sleep(1)
        await channel.put(num)


async def consumer(channel: asyncio.Queue):
    while True:
        item = await channel.get()
        print(f'Got number {item}')


async def main():
    channel = asyncio.Queue()
    asyncio.create_task(consumer(channel))
    await producer(channel)
    print('Done!')

asyncio.run(main())
