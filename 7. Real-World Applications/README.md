WSGI stands for web server gateway interface. 
As the [official documentation of WSGI](https://peps.python.org/pep-3333/) indicates,
it is created standard interface between web servers and python applications (or frameworks).
By [web server](https://en.wikipedia.org/wiki/Web_server), 
we mean software and its underlying hardware that accepts requests via HTTP/HTTPS protocol.

[Gunicorn](https://gunicorn.org/) is a Python WSGI HTTP server 
which is known for running Python applications synchronously.
