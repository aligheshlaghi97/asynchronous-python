# Advanced Techniques
## Error handling and exception propagation in async Python
Handling exceptions in asyncio can be tricky but is a very important concept to understand.
The `asyncio.Task.exception` API is used to raise exceptions within tasks.

The following example, inspired by Jason Brownlee's article 
[found here](https://superfastpython.com/asyncio-task-exceptions/#Example_of_Checking_for_an_Exception_in_a_Failed_Task),
demonstrates how to handle exceptions. In this example, we await longer_task while shorter_task raises an exception.

```python3
async def shorter_task():
    # do quickly
    raise Exception('Some exception happened!')

async def longer_task():
    # do more things here
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
