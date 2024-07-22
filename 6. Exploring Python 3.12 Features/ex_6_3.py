import asyncio
import time


async def main():
    t1 = time.time()
    for _ in range(10 ** 6):
        asyncio.current_task()
    t2 = time.time()
    print(f'It took {t2-t1}s')


asyncio.run(main())
