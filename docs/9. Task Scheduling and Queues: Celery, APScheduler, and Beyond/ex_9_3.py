from ex_9_1 import add
import time


result = add.delay(4, 4)

print(f"Is ready? {result.ready()}")  # Expected to get False at first
time.sleep(0.01)
print(f"Is ready? {result.ready()}")  # Expected to get True at the end
print(f"Result: {result.get(timeout=1)}")
