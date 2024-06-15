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

## Chaining coroutines to compose more complex async workflows


## asyncio Queue and consumer-producer workflows
