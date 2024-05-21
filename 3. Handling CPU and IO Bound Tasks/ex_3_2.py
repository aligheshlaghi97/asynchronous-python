import asyncio
import time
import httpx


async def main():
    t = time.time()
    async with httpx.AsyncClient() as client:
        task1 = asyncio.create_task(client.get('https://www.example.com/'))
        task2 = asyncio.create_task(client.get('https://www.example.com/'))
        task3 = asyncio.create_task(client.get('https://www.example.com/'))
        response1 = await task1
        response2 = await task2
        response3 = await task3
        print(f'response1: {response1}, response2: {response2}, response3: {response3}')
    print(f'It took {time.time() - t} s')

asyncio.run(main())
