import asyncio
import time
import httpx


async def main():
    t = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)
    print(f"it took {time.time() - t} s")
asyncio.run(main())
