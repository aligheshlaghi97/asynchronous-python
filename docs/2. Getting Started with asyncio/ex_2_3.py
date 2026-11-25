import asyncio


async def nested():
    return 42


async def main():
    # Calling nested() only creates a coroutine object.
    # The body does not run, and on Python 3.15 this warns
    # because the coroutine is never awaited:
    # RuntimeWarning: coroutine 'nested' was never awaited
    nested()

    # Await it and the body actually runs:
    print(await nested())  # will print "42".

asyncio.run(main())
