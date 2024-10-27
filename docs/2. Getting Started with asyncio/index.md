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
But later on, we might explore some trickier low-level ones.

## Runners:
we can use runners to a coroutine (as a reminder, sth possible to await) as we saw previously.
We can run `asyncio.sleep` function this way in `async_sleep_for_one_second` coroutine:

```python
# ex_2_1
{% include_relative ex_2_1.py %}
```

We can use `asyncio.run` using context manager to run the above coroutine:
```python
# ex_2_2
{% include_relative ex_2_2.py %}
```
Notice that we will be using python 3.12 and above (for most of the examples) to run our examples through this tutorial.
(e.g. python3.10 will through an error for ex_2_2)

* Note: To grasp the concept of a **context manager** and its functionality with the `with` syntax, 
our goal is to have complete control over our operations. 
For instance, if we need to perform actions like closing a pointer or managing memory without explicitly calling `close`, 
a context manager is handy. In the provided example, the `close` method of the runner will be automatically invoked.

## Awaiting coroutines, creating tasks and using event loop
As we'll see in the following example 
[from asyncio document](https://docs.python.org/3/library/asyncio-task.html#awaitables), 
just by calling a coroutine (without awaiting it), nothing happens:
```python
# ex_2_3
{% include_relative ex_2_3.py %}
```
<br>

Now let's create some tasks and await it. We'll see it works just fine.

```python
# ex_2_4
{% include_relative ex_2_4.py %}
```
<br>

By creating task and awaiting them, we can run multiple tasks concurrently, as `task1` and `task2` in the following example:
```python
# ex_2_5
{% include_relative ex_2_5.py %}
```
<br>

`asyncio.get_running_loop` will return the running event loop of OS thread.


In the following example, we get the event loop, create a task inside that loop and await it to run.
The result is the same with ex_2_4
```python
# ex_2_6
{% include_relative ex_2_6.py %}
```


## Other important APIs of asyncio
We can use `asyncio.TaskGroup` (using context manager) to run tasks concurrently, 
[in example below](https://docs.python.org/3/library/asyncio-task.html#task-groups): 
```python
# ex_2_7
{% include_relative ex_2_7.py %}
```
<br>

We can use `asyncio.wait_for` function to run a coroutine and wait until a timeout.
In this example, the coroutine takes 2 seconds to run completely, but a timeout error will be raised after 1st second.
```python
# ex_2_8
{% include_relative ex_2_8.py %}
```
<br>

This covers the basics of asyncio syntax. 
In the next section, we'll use the APIs we learned here to manage I/O and CPU-bound tasks
