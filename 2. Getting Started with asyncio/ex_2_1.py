import asyncio


async def async_sleep_for_one_second():
    print('stared sleeping for 1 second!')
    await asyncio.sleep(1)
    print('Finished sleeping!')

asyncio.run(async_sleep_for_one_second())
