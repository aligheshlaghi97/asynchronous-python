import asyncio


async def sleep_coro(delay):
    print(f'Started sleeping for {delay} seconds!')
    await asyncio.sleep(delay)
    print(f'Finished sleeping for {delay} seconds!')


async def main():
    try:
        await asyncio.wait_for(sleep_coro(2), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())
