# Getting Started with asyncio
## Overview of the asyncio module in Python

[Asyncio is a library to write concurrent code using the async/await syntax.](https://docs.python.org/3/library/asyncio.html) <br>
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

By the way, it's recommended to delve into the python official documentation for a deeper
understanding of its functioning. However, here, our aim is to simplify the explanation as much as possible.

Asyncio has two types of functions: high-level and low-level. 
High-level functions are easier to use, like the ones we used earlier to run an async task. 
Low-level functions, like event loops we talked about, give more control but are trickier. 
We'll mainly stick to the easier high-level functions to understand asyncio better. 
But later on, we might explore some trickier low-level ones.

## Runners:
we can use runners to a coroutine (as a reminder, sth possible to await) as we saw previously.
We can run `asyncio.sleep` function this way in `async_sleep_for_one_second` coroutine:

```python3
# ex_2_1
async def async_sleep_for_one_second():
    print('stared sleeping for 1 second!')
    await asyncio.sleep(1)
    print('Finished sleeping!')

asyncio.run(async_sleep_for_one_second())
```

We can use `asyncio.run` using context manager to run the above coroutine:
```python3
# ex_2_2
with asyncio.Runner() as runner:
    runner.run(async_sleep_for_one_second())
```
Notice that we will be using python3.12 to run our examples through this tutorial.
(e.g. python3.10 will through an error for ex_2_2)

* Note: To grasp the concept of a **context manager** and its functionality with the `with` syntax, 
our goal is to have complete control over our operations. 
For instance, if we need to perform actions like closing a pointer or managing memory without explicitly calling `close`, 
a context manager is handy. In the provided example, the `close` method of the runner will be automatically invoked.

## Awaiting coroutines, creating tasks and using event loop
As we'll see in the following example 
[from asyncio document](https://docs.python.org/3/library/asyncio-task.html#awaitables), 
just by calling a coroutine (without awaiting it), nothing happens:
```python3
# ex_2_3
async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```
<br>

Now let's create some tasks and await it. We'll see it works just fine.

```python3
# ex_2_4
async def sleep_coro(delay):
    print(f'Started sleeping for {delay} seconds!')
    await asyncio.sleep(delay)
    print(f'Finished sleeping for {delay} seconds!')

async def main():
    task1 = asyncio.create_task(sleep_coro(1))
    await task1

asyncio.run(main())
```
<br>

By creating task and awaiting them, we can run multiple tasks concurrently, as `task1` and `task2` in the following example:
```python3
# ex_2_5
async def main():
    task1 = asyncio.create_task(sleep_coro(1))
    task2 = asyncio.create_task(sleep_coro(1))
    await task1
    await task2

asyncio.run(main())
```
<br>

`asyncio.get_running_loop` will return the running event loop of OS thread.


In the following example, we get the event loop, create a task inside that loop and await it to run.
The result is the same with ex_2_4
```python3
# ex_2_6
async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(sleep_coro(1))
    await task1

asyncio.run(main())
```


## Other important APIs of asyncio
We can use `asyncio.TaskGroup` (using context manager) to run tasks concurrently, 
[in example below](https://docs.python.org/3/library/asyncio-task.html#task-groups): 
```python3
# ex_2_7
async def main():
    print('Before running task group!')
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(sleep_coro(2))
        task2 = tg.create_task(sleep_coro(3))
    print('After running task group!')
    print(f"task1: {task1.result()}, task2: {task2.result()}")
```
<br>

We can use `asyncio.wait_for` function to run a coroutine and wait until a timeout.
In this example, the coroutine takes 2 seconds to run completely, but a timeout error will be raised after 1st second.
```python3
# ex_2_8
async def main():
    try:
        await asyncio.wait_for(sleep_coro(2), timeout=1.0)
    except TimeoutError:
        print('timeout!')
```
<br>

This covers the basics of asyncio syntax. 
In the next section, we'll use the APIs we learned here to manage I/O and CPU-bound tasks
