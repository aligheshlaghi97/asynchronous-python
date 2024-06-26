# Exploring Python 3.12 Features
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

## Highlighting async-related improvements and additions in Python 3.11 and 3.12
### In python 3.11, several important asyncio APIs were added, including:
1. `asyncio.TaskGroup` which was demonstrated in ex_2_7. 
The official documentation recommends using `asyncio.TaskGroup` instead of `asyncio.create_task` and `asyncio.gather` 
by official documentation.
2. `asyncio.Runner` demonstrated in ex_2_2. 
As described in the [official document](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner), 
it is a context manager that simplifies multiple async function calls in the same context.
3. `asyncio.Barrier` demonstrated in ex_4_4, used as a synchronization primitive.

### In python 3.12, some APIs added or enhanced:
1. Added `asyncio.eager_task_factory()` and `asyncio.create_eager_task_factory()` 
functions to allow opting an event loop in to eager task execution, making some use-cases 2x to 5x faster. 
2. Add C implementation of `asyncio.current_task(loop=None)` for 4x-6x speedup.
This API returns the currently running `asyncio.Task` instance, or `None` if no task is running.
If `loop=None` -> `get_running_loop()` used to get the current loop.

## Practical examples demonstrating the use of newer Python versions features in async programming
