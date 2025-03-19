---
layout: default
title: "Chapter 5: Advanced Techniques"
permalink: /chapter5/
---

# Advanced Techniques
## Error handling and exception propagation in async Python
Handling exceptions in asyncio can be tricky but is a very important concept to understand.
The `asyncio.Task.exception` API is used to raise exceptions within tasks.

The following example, inspired by Jason Brownlee's article 
[found here](https://superfastpython.com/asyncio-task-exceptions/#Example_of_Checking_for_an_Exception_in_a_Failed_Task),
demonstrates how to handle exceptions. In this example, we await longer_task while shorter_task raises an exception.

```python
# ex_5_1
{% include_relative ex_5_1.py %}
```
The above code works if `longer_task` takes more time to complete than `shorter_task`. 
Otherwise, if `task1.exception()` is called before `shorter_task` raises an exception,
it will result in an error: `asyncio.exceptions.InvalidStateError: Exception is not set`.

Now let's create our own exception handler and utilize it with previous ex_5_1. 
In order to do it, we've to grab event loop and set the exception handler to it.
```python
# ex_5_2
{% include_relative ex_5_2.py %}
```
<br>

Now let's take a look at an example of canceling a task and catching tbe error inspired by
[this example](https://stackoverflow.com/questions/56052748/python-asyncio-task-cancellation).
```python
# ex_5_3
{% include_relative ex_5_3.py %}
```

## Chaining coroutines using callback and event to compose more complex async workflows
As Jason Brownlee says in his article on 
[Asyncio Coroutine Chaining](https://superfastpython.com/asyncio-coroutine-chaining/#What_is_Coroutine_Chaining),
coroutine chaining refers to the process of 
linking or chaining together multiple coroutines to execute in a specific sequence.
This pattern helps in organizing and managing complex asynchronous workflows.
Consider that done callback is triggered when the task is done.
Let's take a look at an example, inspired by 
[Jason's article](https://superfastpython.com/asyncio-coroutine-chaining/#Example_of_Automatic_Chaining_of_Coroutines_With_Callbacks).
```python
# ex_5_4
{% include_relative ex_5_4.py %}
```
In example above inside main coroutine, we initialize an event, and create task for `task1` and call `add_done_callback`
with `callback1` coroutine. After `task1` finishes, `callback1` is triggered which gets the result of `task1`
and creates task for `task2` with `callback2` as its callback when finished. The result of `task1` is passed to `task2`,
and after `task2` finishes, `callback2` sets the event which lets the `main` coroutine know and finish waiting for that.

Based on that, we can conclude this chain of coroutines to run: <br>
`main` -> `task1` -> `callback1` -> `task2` -> `callback2` -> continue `main`

## asyncio Queue and consumer-producer workflows
A queue is a first-in, first-out (FIFO) data structure with put and get functionalities. 
This means that data can be added (put) to the queue and retrieved (get) in the order it was added, 
ensuring that earlier data is accessed first. In Python, the `collections.deque` class (syncornized) and `queue.Queue` (parallel) class provide this functionality. 
Additionally, for asynchronous programming within coroutines, Python offers the `asyncio.Queue` API.

Let's take a look at 
[this example](https://cprieto.com/posts/2021/07/queues-with-python-asyncio.html) from Cristian Prieto:
```python
# ex_5_5
{% include_relative ex_5_5.py %}
```
As Cristian Prieto says, in this example, `asyncio.Queue` is our way to communicate between the producer of items
and its consumer, it will await until the queue has an item to give us.

### Channels vs Queues
The term channel is used in languages like Golang and Kotlin. Channel is not exactly the same as queue.
In short, a queue is a storage mechanism, while a channel is a communication mechanism (which may internally use a queue).
Actually, a queue is a data structure that stores elements in a first-in, first-out (FIFO) order,
while a channel is a communication mechanism that allows asynchronous data transfer between different parts of a program
and [is used for interprocess communication](https://en.wikipedia.org/wiki/Channel_(programming)).

## asyncio Future
[Future objects are used to bridge low-level callback-based code with high-level async/await code.
](https://docs.python.org/3/library/asyncio-future.html)

![](https://blog.cellenza.com/wp-content/uploads/2023/04/Image5.png)

This image shows the awaitable class inheritance hierarchy. As you can see, every task is actually of type future.
Every `asyncio.Future` has some APIs to call, most important ones are:<br>
`done()`, `set_result(result)`, `result()`<br>
Now let's use these APIs inside an example:
```python
# ex_5_6
{% include_relative ex_5_6.py %}
```

In example above, we create a future, check if it's done or not (using `done()`), 
then set the `result=10` using `set_result(10)`, so the future is done. Moreover, we can await any futures
and get the result of that future.

Also consider that you can call the same APIs on every `asyncio.Task` too.
