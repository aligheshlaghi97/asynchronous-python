import asyncio
import time
import httpx


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        task1 = asyncio.create_task(client.get(url))
        task2 = asyncio.create_task(client.get(url))
        task3 = asyncio.create_task(client.get(url))
        response1 = await task1
        response2 = await task2
        response3 = await task3
        return response1, response2, response3


async def main():
    t = time.time()
    response1, response2, response3 = await fetch_data('https://www.example.com/')
    print(f'response1: {response1}, response2: {response2}, response3: {response3}')
    print(f'It took {time.time() - t} s')

asyncio.run(main())
