---
layout: default
title: "Chapter 3: Handling CPU and I/O Bound Tasks"
permalink: /chapter3/
---

# Handling CPU and I/O Bound Tasks
## CPU-bound vs I/O-bound
So, a very basic question: What are CPU-bound and I/O-bound tasks, and how do they differ from each other?
It's quite simple. CPU-bound tasks are those that primarily consume CPU resources to be handled, while I/O-bound tasks
are related to the input/output devices of your system, such as the network card, keyboard, and others.

A CPU-bound task typically involves intensive mathematical calculations.
In contrast, I/O-bound tasks involve operations like calling different APIs and waiting for their responses.
For example, opening a text file and reading it into memory is also an I/O-bound task.



[Extra Reading: What do the terms CPU-bound and I/O-bound mean?](https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)

## Performing asynchronous I/O operations with asyncio

There are several robust libraries that handle I/O-bound tasks for requesting an endpoint,
such as aiohttp and HTTPX for asynchronous requests, and urllib3 for synchronous ones.

I am going to provide some examples from the HTTPX library on how you can handle several requests
to one host concurrently.
HTTPX can manage both asynchronous and synchronous requests, allowing us to benchmark them.
Here is example 3_1 to get started with HTTPX:


```python
# ex_3_1
{% include_relative ex_3_1.py %}
```

Now let's create some tasks of async requesting to run concurrently, as we learnt in previous section:
```python
# ex_3_2
{% include_relative ex_3_2.py %}
```

Example 3_1 fetches once. Example 3_2 schedules three fetches with `create_task` before awaiting them, so those three requests overlap.

We can also pass the requests to `asyncio.gather`. Unlike example 3_2, the list holds coroutines, and `gather` schedules them.
```python
# ex_3_3
{% include_relative ex_3_3.py %}
```

In this example, a list comprehension creates that list of coroutines,
which is then unpacked into the `gather` function.
The list comprehension creates the list all at once without appending or extending it.

Now, let's look at an example using httpx's synchronous APIs.
It runs the same three requests, to the same host, one after another, so it takes roughly three times longer than examples 3_2 and 3_3.

```python
# ex_3_4
{% include_relative ex_3_4.py %}
```

## Performing CPU operations with multiprocessing

In Python, the multiprocessing library is used to parallelize CPU-bound tasks in other processes, not on the asyncio event loop.
Threads would not speed this adding loop up, because only one thread runs Python bytecode at a time.
The following example starts two worker processes with `Pool(2)`.
`Pool` uses the default way of starting processes. On Linux, Python 3.14 and later default to `forkserver`, and this example does not change that.
The `if __name__ == '__main__'` guard matters for that default, and for `spawn`: the child imports this module, and without the guard it would start another pool.
`spawn` and `forkserver` start a new Python interpreter for the child. That interpreter imports your file again to find `cpu_bound_task`. During that import, `__name__` is not `"__main__"`.
See [Safe importing of main module](https://docs.python.org/3/library/multiprocessing.html#safe-importing-of-main-module).
First, we define a CPU-bound task that simply adds a value to the `_sum` variable.
`Pool.map` passes one argument, so `partial` pre-sets `step`.
Those two processes can run at the same time. Process startup means the speedup will not always be twofold.
```python
# ex_3_5
{% include_relative ex_3_5.py %}
```

## Strategies for balancing CPU and I/O-bound workloads in async Python applications
This is a good article talking about this subject:
[How to Boost Your App Performance with Asyncio](https://blog.cellenza.com/en/software-development/how-to-boost-your-apps-performance-with-asyncio-a-practical-guide-for-python-developers/)

In summary, when dealing with CPU-bound tasks, it's generally advisable to utilize multiprocessing.
One exception is CPU work inside a C extension that releases the GIL: threads can help there.
`Pool.map` cannot be awaited. From a coroutine, CPU work can go through `ProcessPoolExecutor` and [`loop.run_in_executor`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor), and a blocking I/O call can go through [`asyncio.to_thread`](https://docs.python.org/3/library/asyncio-task.html#running-in-threads).
For I/O-bound tasks, the choice typically lies between asyncio and the multithreading modules.
While we didn't cover the multithreading module in this section for simplicity,
it's worth noting that it can also be used for I/O-bound tasks.
If feasible, asyncio is often preferred over threading.
We conclude this section by referencing a table from an article,
which effectively delineates the nuanced distinctions between threading and asyncio.


![Screenshot from 2024-05-24 19-39-15](https://github.com/aligheshlaghi97/asynchronous-python/assets/121802083/935a265a-aa5f-4e35-b311-d9d810e9f5c1)

## Process Creation in Python: Fork vs. Spawn
When working with CPU-bound tasks in Python, you can parallelize workloads by creating child processes using the multiprocessing module.
`fork`, `forkserver`, and `spawn` are all described in [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods).
Two common methods for starting processes are:
  - **Fork**: Duplicates the parent process, inheriting its memory space.
  - **Spawn**: Starts a new, fresh process, without sharing memory with the parent process.

### Fork
The `fork` method copies the parent process's memory, including variables, and works with **copy-on-write (COW)**. This makes it efficient and
[up to 20 times faster than `spawn`](https://superfastpython.com/fork-faster-than-spawn/),
but it can be buggy, especially on macOS. Also, note that fork is not supported on Windows.
Since Python 3.12, `fork` warns when the parent already has other threads. The child keeps only the thread that called `fork`, so locks held by the others can deadlock.

**Copy-on-write** here means that fork uses parent memory when reading but creates a copy of that memory when it needs to modify.

To use `fork`, simply call `multiprocessing.set_start_method('fork')` during initialization.

### Forkserver
`forkserver` also copies a process, like `fork`, but it does not copy your running program.
Python starts a small server process first, and that server forks each child.
The child therefore does not inherit the parent's threads, which is the fragile part of `fork`.
It is the default on Linux in Python 3.14 and later.

### Spawn
The `spawn` method creates a fresh process, which starts execution from the very beginning.
This method is slower but avoids the potential pitfalls of shared memory between parent and child processes.

This is the default method to create a child process on **Windows** and **macOS**.

To use `spawn`, simply call `multiprocessing.set_start_method('spawn')` during initialization.
