# Synchronization and Coordination
## Managing shared resources and avoiding race conditions
So what are race conditions and how do they happen?

As [this link](https://www.techtarget.com/searchstorage/definition/race-condition) says:
Race conditions are most commonly associated with computer science and programming. 
They occur when two computer program processes, or threads,
attempt to access the same resource at the same time and cause problems in the system.

Imagine two processes attempting to increment a shared variable, `a = 0`, each by `1`. 
The expected result should be `2`. 
However, there is a possibility that both processes read the initial value of `0` into their memory simultaneously. 
Consequently, each process adds `1` to `0`,
resulting in the variable a being incorrectly set to `1` instead of the correct value of `2`.

Below you can see a similar example (with some minor changes) from Jason Brownlee in 
[SuperFastPython for asyncio race conditions](https://superfastpython.com/asyncio-race-conditions/):
```python3
# ex_4_1
async def task():
    global value
    tmp = value
    await asyncio.sleep(0.01)
    tmp = tmp + 1
    await asyncio.sleep(0.01)
    value = tmp

async def main():
    global value
    value = 0
    coroutines = [task() for _ in range(10000)]
    await asyncio.gather(*coroutines)
    print(value)
```
In above example, variable `value` must be `10000` but it's `1` in the end.
This race condition happens due to suspending the `task` coroutine using `asyncio.sleep` for 0.01s.

## Synchronization primitives: locks, semaphores, and barriers

To solve the problem above, we can use `asyncio.Lock`.
[An asyncio lock can be used to guarantee exclusive access to a shared resource.](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock)

We can use such a syntax to use locks:
```python3
# ex_4_2
async def task(lock):
    async with lock:
        # access shared state

async def main():
    lock = asyncio.Lock()
    coroutines = [task(lock) for _ in range(10000)]
    await asyncio.gather(*coroutines)
```
As provided in ex_4_2, a lock created inside `main` and passed to `task` coroutine. 
For fast response, 0.01s delay decreased to 0.