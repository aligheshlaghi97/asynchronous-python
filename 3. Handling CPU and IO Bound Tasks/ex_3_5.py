import time
from multiprocessing import Pool
from functools import partial


def cpu_bound_task(a: int, n: int) -> float:
    _sum = 0
    for number in range(n):
        _sum += a
    return _sum


t = time.time()
value = cpu_bound_task(2, 100000000)
print(f'value: {value}')
value = cpu_bound_task(2, 100000000)
print(f'It took without multiprocessing {time.time() - t} s')
print(f'value: {value}')

cpu_bound_partial = partial(cpu_bound_task, 2)

with Pool(2) as p:
    t = time.time()
    value = p.map(cpu_bound_partial, [100000000, 100000000])
    print(f'It took with multiprocessing {time.time() - t} s')
    print(f'value: {value}')
