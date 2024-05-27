# Synchronization and Coordination
## Managing shared resources and avoiding race conditions
So what are race conditions and how do they happen?

As [this link](https://www.techtarget.com/searchstorage/definition/race-condition) says:
Race conditions are most commonly associated with computer science and programming. 
They occur when two computer program processes, or threads,
attempt to access the same resource at the same time and cause problems in the system.

Imagine two processes attempting to increment a shared variable, `a = 0`, each by `1`. 
The expected result should be `2`. 
However, there is a possibility that both processes read the initial value of `0` into their memory simultaneously. 
Consequently, each process adds `1` to `0`,
resulting in the variable a being incorrectly set to `1` instead of the correct value of `2`.
