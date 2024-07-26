import asyncio


async def main():
    future = asyncio.Future()
    print(f'future status is done: {future.done()}')
    future.set_result(10)
    print(f'future status is done: {future.done()}, future result: {future.result()}')
    result = await future
    print(f'future result after being awaited: {result}')


asyncio.run(main())
