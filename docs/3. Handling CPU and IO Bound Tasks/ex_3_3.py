import asyncio
import time
import httpx


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for _ in range(3)]
        obj = await asyncio.gather(*tasks)
        return obj


async def main():
    t = time.time()
    obj = await fetch_data('https://www.example.com/')
    print(f'obj: {obj}, obj type: {type(obj)}')
    print(f'It took {time.time() - t} s')

asyncio.run(main())
