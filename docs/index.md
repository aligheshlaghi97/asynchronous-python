---
layout: default
title: "Async Python Playground"
permalink: /
---

# Async Python Playground

Welcome to the Async Python Playground repository! 🚀

This repository is a comprehensive guide to mastering asynchronous programming in Python,
covering core concepts, practical tools, and advanced techniques. 
From the fundamentals of asyncio to alternative libraries like AnyIO and Trio,
as well as task scheduling solutions such as Celery and APScheduler,
this repository provides a one-stop resource for exploring the async Python ecosystem.

Whether you're a beginner eager to dive into async programming
or an experienced developer looking to refine your skills and explore emerging patterns,
this repository has you covered.

## Key Features:

**Structured Content:** Tutorials and examples covering a wide range of async Python topics.<br />
**Clear Documentation:** Detailed explanations to help you understand concepts and best practices.<br />
**Latest Python Features:** Highlights of async improvements in Python 3.11, 3.12, and 3.13.<br />
**Hands-On Learning:** Try out code examples to build practical async skills.<br />
**Collaborative Community:** Share ideas and contribute to the growing async Python ecosystem.<br />

## Table of Contents:

1. * **Introduction to Asynchronous Programming**
     - What is asynchronous programming?
     - Thread vs process, Concurrency vs parallelism, GIL
     - Event loops and coroutines

2. * **Getting Started with asyncio**
     - Overview of the asyncio module in Python
     - Runners
     - Awaiting coroutines, creating tasks and using event loop
     - Other important APIs of asyncio

3. * **Handling CPU and I/O Bound Tasks**
     - CPU-bound vs I/O-bound
     - Performing asynchronous I/O operations with asyncio and httpx
     - Performing asynchronous CPU operations
     - Strategies for balancing CPU and I/O-bound workloads in async Python applications
     - Process Creation in Python: Fork vs. Spawn

4. * **Synchronization and Coordination**
     - Managing shared resources and avoiding race conditions
     - Synchronization primitives: locks, semaphores, and barriers
     - Coordinating asynchronous tasks with asyncio's synchronization tools

5. * **Advanced Techniques**
     - Error handling and exception propagation in async Python
     - Chaining coroutines using callback and event to compose more complex async workflows
     - asyncio Queue and consumer-producer workflows
     - asyncio Future

6. * **Exploring Features of New Python Versions**
     - Overview of new features and enhancements in Python 3.12
     - Highlighting async-related improvements and additions in Python 3.11, 3.12 and 3.13
     - Practical examples demonstrating the use of newer Python versions features in async programming

7.  * **Web Applications**
      - ASGI vs. WSGI: Understanding the differences and benefits
      - Building RESTful APIs with async Python: Introduction to Starlette microframework

8. * **Introduction to AnyIO and Trio**
      - What Are AnyIO and Trio?
      - Exploring Trio
      - Getting Started with AnyIO
      - Integrating AnyIO and Trio into Existing Projects
      - Best Practices and Advanced Concepts

9. * **Task Scheduling and Queues: Celery, APScheduler, and Beyond**
      - Introduction to Task Scheduling and Queues
      - Getting Started with Celery
      - Lightweight Scheduling with APScheduler
      - Choosing Between Celery, APScheduler, and Alternatives
      - Best Practices and Real-World Examples
