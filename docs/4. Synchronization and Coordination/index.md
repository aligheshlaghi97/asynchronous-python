---
layout: default
title: "Chapter 4: Synchronization and Coordination"
permalink: /chapter4/
---

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
```python
# ex_4_1
{% include_relative ex_4_1.py %}
```
In above example, variable `value` must be `10000` but it's `1` in the end.
This race condition happens due to suspending the `task` coroutine using `asyncio.sleep` for 0.01s.

## Synchronization primitives: locks, semaphores, and barriers
### Locks
To solve the problem above, we can use `asyncio.Lock`.
[An asyncio lock can be used to guarantee exclusive access to a shared resource.](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock)

We can use such a syntax to use locks:
```python
# ex_4_2
{% include_relative ex_4_2.py %}
```
As provided in ex_4_2, a lock created inside `main` and passed to `task` coroutine. 
For fast response, 0.01s delay decreased to 0.

### Semaphores
To limit access to some resources, semaphores are used. 
I'll bring the example from [this article](https://medium.com/@kalmlake/async-io-in-python-sync-primitives-19524a10b9da)
(with some minor changes) to illustrate how a semaphore works.
```python
# ex_4_3
{% include_relative ex_4_3.py %}
```
Running above example, we want to access a limited resouce for 4 time. 
We see that only two acquisitions of limited resource happens at first. 
Then it will sleep for 1s and after releasing the resources the remaining two acquisitions happen.

### Barriers
[As official documents says:](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier) 
A barrier is a simple synchronization primitive that allows to block until parties number of tasks are waiting on it.
Tasks can wait on the `wait()` method and would be blocked until the specified number of tasks end up waiting on `wait()`

```python
# ex_4_4
{% include_relative ex_4_4.py %}
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


```python
# ex_4_5
{% include_relative ex_4_5.py %}
```
In the example above, the main thread will sleep for 1 second before setting the event. 
`asyncio.Condition` is similar to an event but includes lock methods. <br>

Also Jason Brownlee says in 
[his article about asyncio condition](https://superfastpython.com/asyncio-condition-variable/#What_is_an_Asyncio_Condition_Variable):
In concurrency, a condition allows multiple threads to be notified about some result.
