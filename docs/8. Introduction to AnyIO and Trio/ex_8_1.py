import asyncio


async def coro_a():
    await asyncio.sleep(2)


async def coro_b():
    await asyncio.sleep(0.1)


async def fn():
    task_a = asyncio.create_task(coro_a())
    task_b = asyncio.create_task(coro_b())

    return await task_a
