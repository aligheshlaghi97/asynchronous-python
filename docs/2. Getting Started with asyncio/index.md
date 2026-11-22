---
layout: default
title: "Chapter 2: Getting Started with asyncio"
permalink: /chapter2/
---

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
Later on, we go into the trickier low-level ones too: event-loop handlers, done callbacks, and `asyncio.Future`.

## Runners:
we can use runners to run a coroutine, as we saw previously.
A coroutine is the object returned by an `async def` function.
A task and a future can also be awaited, but they are not coroutines.
We can start `async_sleep_for_one_second` with `asyncio.run`. Inside it, we await `asyncio.sleep`:

```python
# ex_2_1
{% include_relative ex_2_1.py %}
```

We can use `asyncio.Runner` as a context manager and call `runner.run` to run the above coroutine:
```python
# ex_2_2
{% include_relative ex_2_2.py %}
```
Notice that we will be using Python 3.15 to run the examples through every chapter of this tutorial.
(e.g. Python 3.10 will throw an error for ex_2_2)

* Note: A **context manager** and the `with` syntax run setup and cleanup around a block of code.
In the example above, leaving the `with` block calls `runner.close()`, which closes the runner and its event loop.
We do not have to call `close` ourselves.

## Awaiting coroutines, creating tasks and using event loop
As we'll see in the following example 
[from asyncio document](https://docs.python.org/3/library/asyncio-task.html#awaitables), 
just by calling a coroutine (without awaiting it), its body does not run.
On Python 3.15 that call also reports `RuntimeWarning: coroutine 'nested' was never awaited`.
Awaiting it runs the body and prints `42`:
```python
# ex_2_3
{% include_relative ex_2_3.py %}
```
<br>

Now let's create some tasks and await them. We'll see it works just fine.

```python
# ex_2_4
{% include_relative ex_2_4.py %}
```
<br>

By creating tasks and awaiting them, we can run multiple tasks concurrently, as `task1` and `task2` in the following example.
Both tasks are created before either one is awaited. `create_task` schedules them on the event loop right away, so they overlap while `main` waits.
Awaiting `task1` and then `task2` does not run them one after the other:
```python
# ex_2_5
{% include_relative ex_2_5.py %}
```
<br>

`asyncio.get_running_loop` will return the running event loop of the current OS thread.


In the following example, we get that loop with `asyncio.get_running_loop`, create a task inside it and await it to run.
The result is the same as ex_2_4
```python
# ex_2_6
{% include_relative ex_2_6.py %}
```


## Other important APIs of asyncio
We can use `asyncio.TaskGroup` with `async with` to run tasks concurrently,
[in example below](https://docs.python.org/3/library/asyncio-task.html#task-groups).
`main` waits there until both tasks finish, then prints their results: 
```python
# ex_2_7
{% include_relative ex_2_7.py %}
```
<br>

We can use `asyncio.wait_for` to wait until a coroutine finishes or a timeout hits, whichever comes first.
In this example the coroutine takes 2 seconds, so after 1 second it is cancelled and `TimeoutError` is raised. `Finished sleeping for 2 seconds!` never prints.
```python
# ex_2_8
{% include_relative ex_2_8.py %}
```
<br>

This covers the basics of asyncio syntax. 
In the next section, we'll use the APIs we learned here to manage I/O and CPU-bound tasks
