import asyncio


async def sleep_coro(delay):
    print(f'Started sleeping for {delay} seconds!')
    await asyncio.sleep(delay)
    print(f'Finished sleeping for {delay} seconds!')
    return delay


async def main():
    print('Before running task group!')
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(sleep_coro(2))
        task2 = tg.create_task(sleep_coro(3))
    print('After running task group!')
    print(f"task1: {task1.result()}, task2: {task2.result()}")

asyncio.run(main())
