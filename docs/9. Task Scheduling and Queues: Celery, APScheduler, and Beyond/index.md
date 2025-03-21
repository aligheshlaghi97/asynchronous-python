---
layout: default
title: "Chapter 9: Task Scheduling and Queues: Celery and APScheduler"
permalink: /chapter9/
---

# Task Scheduling and Queues: Celery and APScheduler
## Introduction to Task Scheduling and Queues

Task scheduling and message queues are essential for handling long-running tasks,
periodic jobs, and inter-component communication in modern applications.
They help improve scalability, resilience, and efficiency
by decoupling workflows and managing workloads asynchronously.

Libraries like `Celery` and `APScheduler` are popular tools for implementing task scheduling and queuing in Python.
They allow developers to offload tasks, schedule recurring jobs, and handle retries seamlessly.
In this section, we’ll explore these tools and learn how to design scalable, asynchronous task systems.

## Getting Started with Celery

First install `Celery` on your system with `pip`.
Then you have to install `RabbitMQ` on your system or setup using docker and make sure it is enabled.
You can use Celery's official documentation hints like
[first steps with Celery](https://docs.celeryq.dev/en/latest/getting-started/first-steps-with-celery.html#rabbitmq)
or [backends and brokers-RabbitMQ](https://docs.celeryq.dev/en/latest/getting-started/backends-and-brokers/rabbitmq.html)
to setup and use celery and RabbitMQ together.

Then we create three python files.
In first one, we initiate backend and broker of celery.
```python
# ex_9_1
{% include_relative ex_9_1.py %}
```

In the second one, `ex_9_2`, we put the `add(4, 4)` inside a celery queue to run.
Then get its result and check if it ready or not.

```python
# ex_9_2
{% include_relative ex_9_2.py %}
```

In the third file, `ex_9_3`, we put the task inside queue, using `delay` function
(`apply_async` can be used too)
and then sleep to get the celery task's result and check if it ready or not.
```python
# ex_9_3
{% include_relative ex_9_3.py %}
```

In order to run above pieces of code, go to chapter9's directory
and run the command below:
```shell
celery -A ex_9_1 worker --loglevel=INFO
```

And then run `ex_9_2.py` and `ex_9_3.py` modules separately (in other shell):
```shell
python ex_9_2.py
python ex_9_3.py
```

If you want to run the task after `t` seconds of non-blocking delay, use `apply_async` this way:
```python
# ex_9_4
{% include_relative ex_9_4.py %}
```

### **Some important points on running Celery worker**
 1. The following command determines the number of workers that can be forked/spawned:
 ```shell
 ulimit -n
 ```
 This number is actually the maximum number of
 [file descriptors](https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms)
 that can be open at any point of time.

 2. By running Celery's worker using `celery -A ex_9_1 worker`,
 there are `n` number of processes forked/spawned by default, where `n` is the number of CPU cores.
 You can determine this by running `pgrep celery` command (which returns their PIDs).

 3. There are two important inputs for running celery worker, `concurrency` and `autoscale`:
 `concurrency` is used to determine the number of processes to be forked/spawned by celery worker
 (which has an upper-bound of maximum number of file descriptors under the hood).
 `autoscale` limits the number of forked/spawned processes between two numbers
 and adjust that number automatically based on the incoming load.

It's also notable that I've inspired and borrowed so much from
[Daksh Gupta's tutorial on Celery](https://www.youtube.com/watch?v=v-Snbz3WmJU).

## Lightweight Scheduling with APScheduler
APScheduler is a relatively simple scheduler library for Python.
It provides Cron-style scheduling and some interval based scheduling.

As the [APScheduler official document](https://apscheduler.readthedocs.io/en/3.x/) states,
APScheduler has four compnents:
1. Trigger: Used to determine when to run the task and has three types:
    - a. Date
    - b. Interval
    - b. Cron
2. Job Store: Saves the scheduled jobs in memory or database.
3. Executor: Handles running of the jobs, using thread or process pool.
4. Scheduler: Binds all things together and helps with configuring the job stores and executors.

Now let's see an example of a simple periodic task using APScheduler from
[Keshav Manglore](https://medium.com/@keshavmanglore/advanced-python-scheduler-scheduling-tasks-with-ap-scheduler-in-python-8c7998a4f116)
which runs every five seconds:
```python
# ex_9_5
{% include_relative ex_9_5.py %}
```

## Choosing Between Celery, APScheduler, and Alternatives

[This link](https://rocketry.readthedocs.io/en/stable/rocketry_vs_alternatives.html) provides a very
useful comparison between different scheduling tools in Rocketry document that worth paying attention.

### When to use APScheduler?
 - If you need simple, in-memory task scheduling inside an async app.
 - If your tasks are lightweight and don’t require distributed execution.

### When to use Celery?
 - If you need reliable background task execution with retries.
 - If you need distributed task processing with multiple workers.
