import time
from multiprocessing import Pool
from functools import partial


def cpu_bound_task(a: int, n: int) -> int | float:
    _sum = 0
    for number in range(n):
        _sum += a
    return _sum


def without_multiprocessing(step: int, value: int) -> tuple[int, int, float]:
    t = time.time()
    value1 = cpu_bound_task(step, value)
    value2 = cpu_bound_task(step, value)
    time_taken = time.time() - t

    return value1, value2, time_taken


def with_multiprocessing(step: int, value: int) -> tuple((int, int, float)):
    cpu_bound_partial = partial(cpu_bound_task, step)

    with Pool(2) as p:
        t = time.time()
        values = p.map(cpu_bound_partial, [value, value])
        time_taken = time.time() - t

    return *values, time_taken


def main() -> None:
    value1, value2, time_taken_without_mp = without_multiprocessing(step=2, value=100000000)
    print(f'Without multiprocessing, value1: {value1}, value2: {value2}')
    print(f'time taken: {time_taken_without_mp} s')
    print('======================================')
    value1, value2, time_taken_with_mp = with_multiprocessing(step=2, value=100000000)
    print(f'With multiprocessing, value1: {value1}, value2: {value2}')
    print(f'time taken: {time_taken_with_mp} s')


if __name__ == '__main__':
    main()
