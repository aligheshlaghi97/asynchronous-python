import asyncio


async def cancel_me():
    await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(cancel_me())
    await asyncio.sleep(0.01)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())
