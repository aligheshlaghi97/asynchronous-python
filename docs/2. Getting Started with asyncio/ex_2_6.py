import asyncio


async def sleep_coro(delay):
    print(f'Started sleeping for {delay} seconds!')
    await asyncio.sleep(delay)
    print(f'Finished sleeping for {delay} seconds!')


async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(sleep_coro(1))
    await task1

asyncio.run(main())
