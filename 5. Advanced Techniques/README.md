# Advanced Techniques
## Error handling and exception propagation in async Python
Handling exceptions in asyncio can be tricky but is a very important concept to understand.
The `asyncio.Task.exception` API is used to raise exceptions within tasks.

The following example, inspired by Jason Brownlee's article 
[found here](https://superfastpython.com/asyncio-task-exceptions/#Example_of_Checking_for_an_Exception_in_a_Failed_Task),
demonstrates how to handle exceptions. In this example, we await longer_task while shorter_task raises an exception.

```python3
# ex_5_1
async def shorter_task():
    # do something quickly
    raise Exception('Some exception happened!')

async def longer_task():
    # do something that takes long
    ...

async def main():
    task1 = asyncio.create_task(shorter_task())
    task2 = asyncio.create_task(longer_task())
    await task2
    ex = task1.exception()
    print(f'Exception: {ex}')
```
The above code works if `longer_task` takes more time to complete than `shorter_task`. 
Otherwise, if `task1.exception()` is called before `shorter_task` raises an exception,
it will result in an error: `asyncio.exceptions.InvalidStateError: Exception is not set`.

Now let's create our own exception handler and utilize it with previous ex_5_1. 
In order to do it, we've to grab event loop and set the exception handler to it.
```python3
# ex_5_2
def exception_handler(loop, context):
    ex = context['exception']
    print(f'Exception: {ex}')

async def shorter_task():
    ...

async def longer_task():
    ...

async def main():
    print('Main coroutine started!')
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(exception_handler)
    task1 = asyncio.create_task(shorter_task())
    task2 = asyncio.create_task(longer_task())
    await task2
    print('Main coroutine done!')

```
<br>

Now let's take a look at an example of canceling a task and catching tbe error inspired by
[this example](https://stackoverflow.com/questions/56052748/python-asyncio-task-cancellation).
```python3
# ex_5_3
async def cancel_me():
    await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(cancel_me())
    await asyncio.sleep(0.01)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")
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
```python3
# ex_5_4
async def task1():
    print('>task1()')
    await asyncio.sleep(1)
    return 1

async def task2(data):
    print(f'>task2() got {data}')
    await asyncio.sleep(1)

def callback2(task):
    global event
    event.set()

def callback1(task):
    result = task.result()
    second_task = asyncio.create_task(task2(result))
    second_task.add_done_callback(callback2)

async def main():
    global event
    event = asyncio.Event()
    first_task = asyncio.create_task(task1())
    first_task.add_done_callback(callback1)
    await event.wait()
```
In example above inside main coroutine, we initialize an event, and create task for `task1` and call `add_done_callback`
with `callback1` coroutine. After `task1` finishes, `callback1` is triggered which gets the result of `task1`
and creates task for `task2` with `callback2` as its callback when finished. The result of `task1` is passed to `task2`,
and after `task2` finishes, `callback2` sets the event which lets the `main` coroutine know and finish waiting for that.

Based on that, we can conclude this chain of coroutines to run: <br>
`main` -> `task1` -> `callback1` -> `task2` -> `callback2` -> continue `main`

## asyncio Queue and consumer-producer workflows
A queue is a first-in, first-out (FIFO) data structure with put and get functionalities. 
This means that data can be added (put) to the queue and retrieved (gotten) in the order it was added, 
ensuring that earlier data is accessed first. In Python, the `queue.Queue` class provides this functionality. 
Additionally, for asynchronous programming within coroutines, Python offers the `asyncio.Queue` API.

Let's take a look at 
[this example](https://cprieto.com/posts/2021/07/queues-with-python-asyncio.html) from Cristian Prieto:
```python3
async def producer(channel: asyncio.Queue):
    for num in range(0, 5):
        await asyncio.sleep(1)
        await channel.put(num)

async def consumer(channel: asyncio.Queue):
    while True:
        item = await channel.get()
        print(f'Got number {item}')

async def main():
    channel = asyncio.Queue()
    cons = asyncio.create_task(consumer(channel))
    await producer(channel)
    print('Done!')
```
As Cristian Prieto says, in this example, `asyncio.Queue` is our way to communicate between the producer of items
and its consumer, it will await until the queue has an item to give us.
