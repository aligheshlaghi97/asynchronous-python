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

import asyncio


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

To understand what is **context manager** and how it works using `with` syntax, the aim is to fully control what we want to run.
e.g. we want to close a pointer (or do sth else) to memory after the job without using `close` syntax, we can use context manager.
The above example will automatically call `close` method of runner.

## Basic syntax and usage of coroutines and event loops



## Writing your first async Python program



## Basic syntax of asyncio
