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


```python3
# ex_3_1
async def main():
    t = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)
    print(f"it took {time.time() - t} s")
```

Now lets create some tasks of async requesting to run concurrently, as we learnt in previous section:
```python3
# ex_3_2
async def main():
    t = time.time()
    async with httpx.AsyncClient() as client:
        task1 = asyncio.create_task(client.get('https://www.example.com/'))
        task2 = asyncio.create_task(client.get('https://www.example.com/'))
        task3 = asyncio.create_task(client.get('https://www.example.com/'))
        response1 = await task1
        response2 = await task2
        response3 = await task3
        print(f'response1: {response1}, response2: {response2}, response3: {response3}')
    print(f'It took {time.time() - t} s')

```

The times recorded in examples 3_1 and 3_2 are very close,
indicating that example 3_2 is running the requests concurrently.

We can also gather all the tasks using `asyncio.gather`, doing literally the same thing as in example 3_2.
```python3
# ex_3_3
async def main():
    url = 'https://www.example.com/'
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for _ in range(3)]
        obj = await asyncio.gather(*tasks)
```

In this example, a list comprehension is utilized to create the `task` list,
which is then unpacked into the `gather` function.
The list comprehension creates the list all at once without appending or extending it.

Now, let's look at an example using httpx's synchronous APIs,
which takes roughly three times longer than the previous examples.

```python3
# ex_3_4
url = 'https://www.example.org/'
response1 = httpx.get(url)
response2 = httpx.get(url)
response3 = httpx.get(url)
```

## Performing asynchronous CPU operations

In Python, the multiprocessing library is used to parallelize CPU-bound tasks. 
We achieve this by utilizing just two of our CPU's cores in the following example.
First, we define a CPU-bound task that simply adds a value to the `_sum` variable. 
To utilize the multiprocessing library, we use partial functions, 
which are the same functions with some variables pre-set. 
Running the code in the next example, we see the speed double.
```python3
# ex_3_5
def cpu_bound_task(a: int, n: int) -> float:
    _sum = 0
    for number in range(n):
        _sum += a
    return _sum

t = time.time()
value = cpu_bound_task(2, 100000000)
print(f'value: {value}')
value = cpu_bound_task(2, 100000000)
print(f'It took without multiprocessing {time.time() - t} s')
print(f'value: {value}')

cpu_bound_partial = partial(cpu_bound_task, 2)

with Pool(2) as p:
    t = time.time()
    value = p.map(cpu_bound_partial, [100000000, 100000000])
    print(f'It took with multiprocessing {time.time() - t} s')
    print(f'value: {value}')
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
