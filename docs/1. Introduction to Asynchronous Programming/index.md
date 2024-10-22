---
layout: default
title: "Chapter 1: Introduction to Asynchronous Programming"
permalink: /chapter1/
---

# Introduction to Asynchronous Programming
## What is asynchronous programming?
Starting with a broad question, aren't we? Well, when it comes to asynchronous programming, the goal is to execute multiple tasks within our code simultaneously. 
Think of it like being on a moving train, chatting with friends, and listening to music all at once. This scenario perfectly illustrates the essence of asynchronous action.
<br><br>
[Ben Lutkevich says](https://www.techtarget.com/searchnetworking/definition/asynchronous):<br>
Also known as nonblocking code, asynchronous programming provides opportunities for a program to continue running other code while waiting for a long-running task to complete.

## Thread vs process, Concurrency vs parallelism, GIL
### Thread vs process
[Roderick Bauer says](https://medium.com/@rodbauer/understanding-programs-processes-and-threads-fd9fdede4d88):<br>
Threads are the smallest units capable of independent processing, sharing memory within a process. Conversely, a process possesses its own memory and may encompass multiple threads.

### Concurrency vs Parallelism
Concurrency involves executing various tasks by alternating between them rapidly through time slicing, whereas parallelism entails executing different tasks simultaneously. <br>
[The image says that all](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6BoKUYL2j9SHZV8uY4T_gg.png) <br>
![Screenshot from 2024-05-04 20-43-33](https://github.com/aligheshlaghi97/asynchronous-python/assets/121802083/ee6d54da-d706-446d-b692-5429f02fa47e)


### GIL
A [GIL](https://en.wikipedia.org/wiki/Global_interpreter_lock) 
(global interpreter lock) is a mechanism used in computer-language interpreters to synchronize the execution of threads so that only one native thread can execute basic operations at a time. 
However use of a global interpreter lock in a language effectively limits the amount of parallelism reachable through concurrency of a single interpreter process with multiple threads.

## Event loops and coroutines
### Event loops
The [event loop](https://docs.python.org/3/library/asyncio-eventloop.html) is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.
[Here we see here how it works](https://gist.github.com/kassane/f2330ef44b070f4a5fa9d59c770f68e9) 
![Screenshot from 2024-05-04 21-47-21](https://github.com/aligheshlaghi97/asynchronous-python/assets/121802083/ad98b45c-a159-4ece-b82d-39a2ca78528c)

### coroutines
Coroutines have been described as ["functions whose execution you can pause"](https://en.wikipedia.org/wiki/Coroutine). <br>
This seems confusing, but wait, we will clarify it.
Anything in Python that can be implemented with the ```async def``` statement is a coroutine function. <br>
Here ```func``` is a coroutine function:
```python
async def func():
    pass
```
Then we can run this by awaiting it ```await func()```, or run it from top level by ```asyncio.run(func())```.
