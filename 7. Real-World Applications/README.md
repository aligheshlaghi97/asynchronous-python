# Real-World Applications
## ASGI vs. WSGI: Understanding the differences and benefits
### WSGI and Gunicorn
WSGI stands for web server gateway interface. 
As the [official documentation of WSGI](https://peps.python.org/pep-3333/) indicates,
it is created standard interface between web servers and python applications (or frameworks).
By [web server](https://en.wikipedia.org/wiki/Web_server), 
we mean software and its underlying hardware that accepts requests via HTTP/HTTPS protocol.

[Gunicorn](https://gunicorn.org/) is a Python WSGI HTTP server 
which is known for running Python applications synchronously by default.
Let's see an example of Gunicorn from its official document.

```python
# ex_7_1
def app(environ, start_response):
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
```

In order to run this app, this command can be used:
```shell
$ gunicorn --workers=2 --worker_class='sync' test:app
```

[`workers`](https://docs.gunicorn.org/en/latest/settings.html#workers)
is an important parameter in gunicorn, which is the number of worker processes for handling requests.
2-4 times the number of cores is doc's suggestion.

[`worker_class`](https://docs.gunicorn.org/en/latest/settings.html#worker-class) 
parameter determines different modes of workers, which is `sync` by default.
There are other modes e.g. `gevent` and `eventlet` are  asynchronous workers.

### ASGI and Uvicorn


### The Comparison


## Building REST APIs with async Python: Principles and best practices


## Introduction to Starlette framework for async web applications

## Exploring practical examples of async Python in real-world scenarios
