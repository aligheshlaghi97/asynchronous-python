import asyncio
import time


async def light_coro():
    pass


async def main():
    print('Before running task group!')
    tasks_list = [light_coro() for _ in range(1000000)]
    time0 = time.time()

    tasks = asyncio.gather(*tasks_list)
    await tasks

    print(f'It took {time.time() - time0} to run!')
    print('After running gather without eager task factory!')
    print(f"tasks: {tasks}")

asyncio.run(main())
