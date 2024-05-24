import asyncio
import time
import httpx


async def main():
    t = time.time()
    url = 'https://www.example.com/'
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for _ in range(3)]
        obj = await asyncio.gather(*tasks)
        print(f'obj: {obj}, obj type: {type(obj)}')
    print(f'It took {time.time() - t} s')

asyncio.run(main())
