from ex_9_1 import add


result = add.delay(4, 4)

print(f"Is ready? {result.ready()}")  # Expected to get False at first
print(f"result: {result.get(timeout=1)}")  # Expected to get the sum 4 + 4 = 8
print(f"Is ready? {result.ready()}")  # Expected to get True at the end
