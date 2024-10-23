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
such as aiohttp, Starlette, urllib3, and HTTPX.

I am going to provide some examples from the HTTPX library on how you can handle requests
to different endpoints concurrently.
HTTPX can manage both asynchronous and synchronous requests, allowing us to benchmark them.
Here is example 3_1 to get started with HTTPX:


```python
# ex_3_1
{% include_relative ex_3_1.py %}
```

Now lets create some tasks of async requesting to run concurrently, as we learnt in previous section:
```python
# ex_3_2
{% include_relative ex_3_2.py %}
```

The times recorded in examples 3_1 and 3_2 are very close,
indicating that example 3_2 is running the requests concurrently.

We can also gather all the tasks using `asyncio.gather`, doing literally the same thing as in example 3_2.
```python
# ex_3_3
{% include_relative ex_3_3.py %}
```

In this example, a list comprehension is utilized to create the `task` list,
which is then unpacked into the `gather` function.
The list comprehension creates the list all at once without appending or extending it.

Now, let's look at an example using httpx's synchronous APIs,
which takes roughly three times longer than the previous examples.

```python
# ex_3_4
{% include_relative ex_3_4.py %}
```

## Performing asynchronous CPU operations

In Python, the multiprocessing library is used to parallelize CPU-bound tasks.
We achieve this by utilizing just two of our CPU's cores in the following example.
First, we define a CPU-bound task that simply adds a value to the `_sum` variable.
To utilize the multiprocessing library, we use partial functions,
which are the same functions with some variables pre-set.
Running the code in the next example, we see the speed double.
```python
# ex_3_5
{% include_relative ex_3_5.py %}
```

##Strategies for balancing CPU and I/O-bound workloads in async Python applications
This is a good article talking about this subject:
[How to Boost Your App Performance with Asyncio](https://blog.cellenza.com/en/software-development/how-to-boost-your-apps-performance-with-asyncio-a-practical-guide-for-python-developers/)

In summary, when dealing with CPU-bound tasks, it's generally advisable to utilize multiprocessing,
with some exceptions we'll discuss later.
For I/O-bound tasks, the choice typically lies between asyncio and the multithreading modules.
While we didn't cover the multithreading module in this section for simplicity,
it's worth noting that it can also be used for I/O-bound tasks.
If feasible, asyncio is often preferred over threading.
We conclude this section by referencing a table from an article,
which effectively delineates the nuanced distinctions between threading and asyncio.


![Screenshot from 2024-05-24 19-39-15](https://github.com/aligheshlaghi97/asynchronous-python/assets/121802083/935a265a-aa5f-4e35-b311-d9d810e9f5c1)

## Process Creation in Python: Fork vs. Spawn
When working with CPU-bound tasks in Python, you can parallelize workloads by creating child processes using the multiprocessing module.
Two common methods for starting processes are:
  - **Fork**: Duplicates the parent process, inheriting its memory space.
  - **Spawn**: Starts a new, fresh process, without sharing memory with the parent process.

### Fork
The `fork` method copies the parent process's memory, including variables, and works with **copy-on-write (COW)**. This makes it efficient and
[up to 20 times faster than `spawn`](https://superfastpython.com/fork-faster-than-spawn/),
but it can be buggy, especially on macOS. Also, note that fork is not supported on Windows.

**Copy-on-write** here mean that fork uses parent memory when reading but creates a copy of that memory when it needs to modify.

To use `fork`, simply call `multiprocessing.set_start_method('fork')` during initialization.

### Spawn
The `spawn` method creates a fresh process, which starts execution from the very beginning.
This method is slower but avoids the potential pitfalls of shared memory between parent and child processes.

This is the default method to create a child process on **Windows** and **macOS**.

To use `spawn`, simply call `multiprocessing.set_start_method('spawn')` during initialization.
This is the default method to create a child process on Windows and MacOS.
