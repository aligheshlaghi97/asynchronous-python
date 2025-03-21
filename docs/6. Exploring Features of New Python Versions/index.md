---
layout: default
title: "Chapter 6: Exploring Features of New Python Versions"
permalink: /chapter6/
---

# Exploring Features of New Python Versions
## Overview of new features and enhancements in Python 3.12
As Geir Arne Hjelle says in 
[his tutorial](https://realpython.com/python312-new-features/),
Python 3.12 has the following improvements:
- Better error messages with helpful suggestions and guidance 
- More expressive f-strings that are backed by Python’s PEG parser 
- Optimizations, including inlined comprehensions, for a faster Python 
- A new syntax for type variables that you use to annotate generics 
- Support for the powerful perf profiler on Linux

I won't go into the details of these improvements, but for more information, you can read Geir's article on RealPython 
or consult the 
[official documentation](https://docs.python.org/3/whatsnew/3.12.html).

## Highlighting async-related improvements and additions in Python 3.11, 3.12 and 3.13
### In python 3.11, several important asyncio APIs were added, including:
1. `asyncio.TaskGroup` which was demonstrated in ex_2_7. 
The official documentation recommends using `asyncio.TaskGroup` instead of `asyncio.create_task` and `asyncio.gather` 
by official documentation.
2. `asyncio.Runner` which demonstrated in ex_2_2. 
As described in the [official document](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner), 
it is a context manager that simplifies multiple async function calls in the same context.
3. `asyncio.Barrier` demonstrated in ex_4_4, used as a synchronization primitive.

### In python 3.12, some APIs added or enhanced:
1. Added `asyncio.eager_task_factory()` and `asyncio.create_eager_task_factory()` 
functions to allow opting an event loop in to eager task execution, making some use-cases 2x to 5x faster. 
2. Add C implementation of `asyncio.current_task(loop=None)` for 4x-6x speedup.
This API returns the currently running `asyncio.Task` instance, or `None` if no task is running.
If `loop=None`, then it calls `get_running_loop()` to get the current event loop.

### In Python 3.13 an API for shutdown queues added:
1. Added `asyncio.Queue.shutdown` which will raise `asyncio.QueueShutDown` exception on `put` and `get` calls.

## Practical examples demonstrating the use of newer Python versions features in async programming
Let's start with eager_task_factory as something quite useful in asyncio world.
As [this pull request](https://github.com/python/cpython/pull/104140) (and its corresponding issue) demonstrates, 
using `asyncio.eager_task_factory` can speed up some async-heavy workloads to run up to 4-6 times.

Just take a look at ex_6_1 in which runs nearly 6 times faster than ex_6_2, however the same thing happens in both.
The idea is that we create a light coroutine named `light_coro` (in which we just pass and don't do anything) 
and call it for one million times. We use `eager_task_factory` and `TaskGroup` in first example (ex_6_1)
but use `gather` without `eager_task_factory` in the second one (ex_6_2).
```python
# ex_6_1
{% include_relative ex_6_1.py %}
```

```python
# ex_6_2
{% include_relative ex_6_2.py %}
```
So we see that using `eager_task_factory` can be quite useful.
And the official documentation's recommendation to use `TaskGroup` over `gather` makes sense now.

Now let's talk about the speed-up of `asyncio.current_task` in Python3.12.
In the following example, we call `asyncio.current_task` one million times. 
Interestingly, this code runs nearly six times faster with Python 3.12 compared to other versions. Specifically, 
it takes 0.05 seconds with Python 3.12 versus 0.33 seconds with Python 3.10 in my PC.

```python
# ex_6_3
{% include_relative ex_6_3.py %}
```

This is also an example from `asyncio.Queue.shutdown` usage in python 3.13:
```python
# ex_6_4
{% include_relative ex_6_4.py %}
```
Running example above will raise `asyncio.QueueShutDown` error.
