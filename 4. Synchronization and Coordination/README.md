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
### Locks
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

### Semaphores
To limit access to some resources, semaphores are used. 
I'll bring the example from [this article](https://medium.com/@kalmlake/async-io-in-python-sync-primitives-19524a10b9da)
(with some minor changes) to illustrate how a semaphore works.
```python3
# ex_4_3
async def limited_resource(sem):
    async with sem:
        print("Accessing limited resource")
        await asyncio.sleep(1)
        print("Finished using limited resource")

async def main():
    sem = asyncio.Semaphore(2)
    tasks = [limited_resource(sem) for _ in range(4)]
    await asyncio.gather(*tasks)
```
Running above example, we want to access a limited resouce for 4 time. 
We see that only two acquisitions of limited resource happens at first. 
Then it will sleep for 1s and after releasing the resources the remaining two acquisitions happen.

### Barriers
[As official documents says:](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier) 
A barrier is a simple synchronization primitive that allows to block until parties number of tasks are waiting on it.
Tasks can wait on the `wait()` method and would be blocked until the specified number of tasks end up waiting on `wait()`

```python3
# ex_4_4
async def example_barrier():
    b = asyncio.Barrier(3)
    asyncio.create_task(b.wait())
    asyncio.create_task(b.wait())

    await asyncio.sleep(0)
    print(b)
    await b.wait()
    print(b)
    print("barrier passed")
    await asyncio.sleep(0)
    print(b)
```
Running example above, results in the below response:
```shell
<asyncio.locks.Barrier object at 0x... [filling, waiters:2/3]>
<asyncio.locks.Barrier object at 0x... [draining, waiters:0/3]>
barrier passed
<asyncio.locks.Barrier object at 0x... [filling, waiters:0/3]>
```

## Coordinating asynchronous tasks with asyncio's synchronization tools
We can use a combination of the above methods to coordinate asynchronous tasks or 
leverage more advanced APIs such as `asyncio.Event` or `asyncio.Condition`. 
An example from the [official asyncio documentation](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event)
can help us understand events.


```python3
# ex_4_5
async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    event = asyncio.Event()
    waiter_task = asyncio.create_task(waiter(event))
    await asyncio.sleep(1)
    event.set()
    await waiter_task
```
In the example above, the main thread will sleep for 1 second before setting the event. 
`asyncio.Condition` is similar to an event but includes lock methods. <br>

Also Jason Brownlee says in 
[his article about asyncio condition](https://superfastpython.com/asyncio-condition-variable/#What_is_an_Asyncio_Condition_Variable):
In concurrency, a condition allows multiple threads to be notified about some result.
