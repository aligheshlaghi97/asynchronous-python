import trio


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)
    print("Done!")


async def producer(send_channel):
    async with send_channel:
        for value in range(5):
            await trio.sleep(1)
            await send_channel.send(value)


async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f"Got number {value}")


trio.run(main)
