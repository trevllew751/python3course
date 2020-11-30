from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Executed: {fn.__name__}")
        print(f"Time Elapsed: {end - start}")
        return result

    return wrapper


@speed_test  # equivalent to sum_nums = speed_test(sum_nums)
def sum_nums_gen(to):
    return sum(x for x in range(to))


@speed_test  # equivalent to sum_nums = speed_test(sum_nums)
def sum_nums_lst(to):
    return sum([x for x in range(to)])


print(sum_nums_gen(50))
print(sum_nums_lst(50))
