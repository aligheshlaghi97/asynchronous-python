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

The time it takes in example 3_1 and 3_2 are very close, meaning that example 3_2 is running the requests concurrently.
