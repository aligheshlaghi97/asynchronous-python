---
layout: default
title: "Chapter 8: Introduction to AnyIO and Trio"
permalink: /chapter8/
---

# Introduction to AnyIO and Trio
## What Are AnyIO and Trio?
Let's imagine that our primary objective is achieving concurrency for I/O bound tasks.
While we have been exploring `asyncio` in Python to support this goal,
additional tools such as `anyio` and `trio` offer valuable alternatives for enhancing I/O parallelism
which leverage the benefits of the `Structured Concurrency` design pattern.
Their appeal lies in their user-friendly nature, enhanced features, and reduced learning curve,
making them attractive options for improving task efficiency.

### Why to use them?

 - **Improved Developer Productivity**: Simplified APIs and tools reduce the learning curve and development time.

 - **Cross-Framework Compatibility**: AnyIO ensures that our code can run on different async backends without modification.

 - **Enhanced Safety**: Trio’s structured concurrency model reduces the likelihood of subtle bugs in concurrent code.



## Structured Concurrency Design Pattern
As Jan Plesnik explains [here](https://applifting.io/blog/python-structured-concurrency),
to avoid orphaned tasks—tasks that lose their reference—we need to embrace structured concurrency.
In Python 3.11, the introduction of `asyncio.TaskGroup` provides a way to manage this effectively
Similarly, Trio offers nurseries, which serve the same purpose.
An example of an orphaned task can be seen in the following case, where `task_b` loses its reference.
(Example from Jan's article.)

```python
# ex_8_1
{% include_relative ex_8_1.py %}
```
This image illustrates what happens under the hood
(from [here](https://belief-driven-design.com/looking-at-java-21-structured-concurrency-39a81/)):
![test1](https://github.com/user-attachments/assets/48215a3a-538f-4a0b-8143-34268958d794)

And now imagine this example with `asyncio.TaskGroup` (which is similar to example_2_8).
As you see, both `task_a` and `test_b` will finish and then the task-group context manager exits.

```python
# ex_8_2
{% include_relative ex_8_2.py %}
```

And now we have full control over tasks and this is how it will look like.
![test2](https://github.com/user-attachments/assets/3d82ae86-3fc2-42e6-b342-94bfea9f342b)

## Exploring Trio
`Trio`'s primary aim is to simplify the comprehension and enhance the performance of concurrency operations.
It offers a more efficient GIL and higher-level APIs, resulting in code that is easier to understand and troubleshoot.

Now let's see our first example from [trio's official document](https://trio.readthedocs.io/en/stable/)
and get familiar with it.
As you can see, there is a parent async function which uses nurseries to spawn two child tasks and run them.
```python
# ex_8_3
{% include_relative ex_8_3.py %}
```

A very interesting topic would be to see how `consumer-producer` is handled in `trio`, described in official document
[here](https://trio.readthedocs.io/en/stable/reference-core.html#using-channels-to-pass-values-between-tasks)
and compare it with our `ex_5_5`, a consumer-producer variant in `asyncio`.
`open_memory_channel` is an API used to create queue and manage consumer-producer in `trio`.
Let's rewrite our `ex_5_5` in `trio` syntax:
```python
# ex_8_4
{% include_relative ex_8_4.py %}
```
By utilizing `open_memory_channel`, we get two channels initiated and then call consumer/producer with their respective channels.
Also, the `consumer` and `producer` async functions contain a context manager to signal the completion of the production/consumption processes.


## Getting Started with AnyIO
AnyIO is a handy library that makes async programming easier by letting you write code that works with both `asyncio` and `Trio`.
It hides the differences between these frameworks, so your code runs smoothly no matter which event loop you use.


The starter example from [anyio official document](https://anyio.readthedocs.io/en/stable/tasks.html#creating-and-managing-tasks) is provided here:
```python
# ex_8_5
{% include_relative ex_8_5.py %}
```

It runs on top of `asyncio` and if you want to run it on top of `Trio` just do this in run section:
```python
run(main, backend='trio')
```


## Integrating AnyIO and Trio into Existing Projects





## Best Practices and Advanced Concepts
