import asyncio


async def limited_resource(sem):
    async with sem:
        print("Accessing limited resource")
        await asyncio.sleep(1)
        print("Finished using limited resource")


async def main():
    sem = asyncio.Semaphore(2)
    tasks = [limited_resource(sem) for _ in range(4)]
    await asyncio.gather(*tasks)

asyncio.run(main())
