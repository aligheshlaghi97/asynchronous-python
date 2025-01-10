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
As Jan Plesnik says [here](https://applifting.io/blog/python-structured-concurrency),
if we don't want orphaned tasks (which means a task which lost its reference),
we need to be aware of structured concurrency.
In Python3.11 we saw `asyncio.TaskGroup` earlier which helps us with it.
In `Trio` there is `nurseries` which help us with it.
As an example of orphaned tasks, you can imagine `task_b` in the following example. (example from Jan's article)

```python
{% include_relative ex_8_1.py %}
```

## Exploring Trio
`Trio`'s primary aim is to simplify the comprehension and enhance the performance of concurrency operations.
It offers a more efficient GIL and higher-level APIs, resulting in code that is easier to understand and troubleshoot.


## Getting Started with AnyIO




## Integrating AnyIO and Trio into Existing Projects





## Best Practices and Advanced Concepts
