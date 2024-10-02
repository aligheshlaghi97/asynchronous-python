import asyncio
import time
import httpx


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response


async def main():
    t = time.time()
    response = await fetch_data('https://www.example.com/')
    print(f"response is: {response}")
    print(f"it took {time.time() - t} s")

asyncio.run(main())
