import asyncio


async def main():
    queue = asyncio.Queue()
    await queue.put(1)
    queue.shutdown()
    await queue.put(2)

asyncio.run(main())
