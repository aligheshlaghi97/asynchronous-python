import anyio


async def producer(sender):
    async with sender:
        for value in range(5):
            await sender.send(value)
            await anyio.sleep(1)


async def consumer(receiver):
    async with receiver:
        async for value in receiver:
            print(f'Got number {value}')
            await anyio.sleep(1)


async def main():
    sender, receiver = anyio.create_memory_object_stream()
    async with anyio.create_task_group() as tg:
        async with sender, receiver:
            tg.start_soon(producer, sender.clone())
            tg.start_soon(consumer, receiver.clone())


anyio.run(main)
