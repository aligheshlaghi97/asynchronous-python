import asyncio


async def task1():
    print('>task1()')
    await asyncio.sleep(1)
    return 1


async def task2(data):
    print(f'>task2() got {data}')
    await asyncio.sleep(1)


def callback2(task):
    global event
    event.set()


def callback1(task):
    result = task.result()
    second_task = asyncio.create_task(task2(result))
    second_task.add_done_callback(callback2)


async def main():
    global event
    event = asyncio.Event()
    first_task = asyncio.create_task(task1())
    first_task.add_done_callback(callback1)
    await event.wait()
    print('Main: chain is done')


asyncio.run(main())
