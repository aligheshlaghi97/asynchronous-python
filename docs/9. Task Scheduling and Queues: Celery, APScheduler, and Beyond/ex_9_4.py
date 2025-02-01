from ex_9_1 import add
import time

t = 2  # Expected to run add function after 2 seconds
result = add.apply_async((4, 4), countdown=t)

print(f"Is ready? {result.ready()}")  # Expected to get False at first
time.sleep(2.1)
print(f"Is ready? {result.ready()}")  # Expected to get True at the end
print(f"Result: {result.get(timeout=1)}")
