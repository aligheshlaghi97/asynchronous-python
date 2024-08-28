# Real-World Applications
## ASGI vs. WSGI: Understanding the differences and benefits
### WSGI and Gunicorn
WSGI stands for web server gateway interface. 
As the [official documentation of WSGI](https://peps.python.org/pep-3333/) indicates,
it has created standard interface between web servers and python applications (or frameworks).
By [web server](https://en.wikipedia.org/wiki/Web_server), 
we mean software and its underlying hardware that accepts requests via HTTP/HTTPS protocol, e.g. Nginx and Apache.

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
$ gunicorn --workers=2 --worker_class='sync' ex_7_1:app
```

[`workers`](https://docs.gunicorn.org/en/latest/settings.html#workers)
is an important parameter in gunicorn, which is the number of worker processes for handling requests.
2-4 times the number of cores is doc's suggestion.

[`worker_class`](https://docs.gunicorn.org/en/latest/settings.html#worker-class) 
parameter determines different modes of workers, which is `sync` by default.
There are other modes e.g. `gevent` and `eventlet` are  asynchronous workers.

Moreover, you've to consider that Gunicorn only supports HTTP/1.1.

### ASGI and Uvicorn
[ASGI](https://asgi.readthedocs.io/en/latest/) (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI,
intended to provide a standard interface between async-capable Python applications and web server.
It also supports HTTP/1.1, HTTP/2 and websocket connection.

[Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python.
Uvicorn uses the [ASGI specification](https://asgi.readthedocs.io/en/latest/) for interacting with an application.

Let's see an example of python application which runs with uvicorn from official document:
```python
# ex_7_2
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
```
You can find the meaning of each `scope`, `receive` and `send` [here](https://www.uvicorn.org/#the-asgi-interface).

In order to run this app, use the command below:
```shell
uvicorn ex_7_2:app
```
To know about additional parameters to pass, [this link](https://www.uvicorn.org/#command-line-options) is helpful.
## Building RESTful APIs with async Python: Introduction to Starlette microframework
As described [here](https://positiwise.com/blog/difference-between-restapi-restful-api),
a RESTful API is an Application Programming Interface (API) 
that uses the Representational State Transfer (REST) architectural style for its implementation. 
[Statelessness](https://aws.amazon.com/what-is/restful-api/#:~:text=discover%20more%20resources.-,Statelessness,-In%20REST%20architecture) 
is one of its main characteristics.

According to [this link](https://fastapi.tiangolo.com/benchmarks/), FastAPI uses Starlette internally
