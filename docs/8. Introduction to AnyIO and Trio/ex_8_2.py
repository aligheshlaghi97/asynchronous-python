import asyncio


async def sleep_coro(delay):
    print(f"Started sleeping for {delay} seconds!")
    await asyncio.sleep(delay)
    print(f"Finished sleeping for {delay} seconds!")
    return delay


async def main():
    print('Before running task group!')
    async with asyncio.TaskGroup() as tg:
        task_a = tg.create_task(sleep_coro(2))
        task_b = tg.create_task(sleep_coro(1))
    print("After running task group!")
    print("Both tasks finished!")
    print(f"Results are: (task_a: {task_a.result()}, task_b: {task_b.result()})")

asyncio.run(main())
