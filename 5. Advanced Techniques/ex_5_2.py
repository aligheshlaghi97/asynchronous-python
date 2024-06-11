import asyncio


def exception_handler(loop, context):
    ex = context['exception']
    print(f'Exception: {ex}')


async def shorter_task():
    print('Executing the task to raise an exception!')
    await asyncio.sleep(0.01)
    raise Exception('Some exception happened!')


async def longer_task():
    print('Executing the task which will complete!')
    await asyncio.sleep(1)  # sleep more than shorter_task
    print('longer_task is done!')


async def main():
    print('Main coroutine started!')
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(exception_handler)
    task1 = asyncio.create_task(shorter_task())
    task2 = asyncio.create_task(longer_task())
    await task2
    print('Main coroutine done!')


asyncio.run(main())
