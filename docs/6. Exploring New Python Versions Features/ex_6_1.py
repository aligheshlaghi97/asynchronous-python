import asyncio
import time


async def light_coro():
    pass


async def main():
    print('Before running task group!')
    time0 = time.time()
    asyncio.get_event_loop().set_task_factory(asyncio.eager_task_factory)
    async with asyncio.TaskGroup() as tg:
        for _ in range(1000000):
            tg.create_task(light_coro())
    print(f'It took {time.time() - time0} to run!')
    print('After running task group with eager task factory!')

asyncio.run(main())
