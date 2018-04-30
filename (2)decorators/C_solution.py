import functools
import time


def profiler(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        a = time.time()
        if not hasattr(wrapper, "iter_in"):
            wrapper.iter_in = 0
        if not hasattr(wrapper, "iter_out"):
            wrapper.iter_out = 0
        if wrapper.iter_in == wrapper.iter_out and wrapper.iter_in != 0:
            wrapper.iter_in = wrapper.iter_out = 0
        wrapper.iter_in += 1
        f = func(*args, **kwargs)
        wrapper.iter_out += 1
        if wrapper.iter_in == wrapper.iter_out:
            wrapper.calls = wrapper.iter_in
            wrapper.last_time_taken = time.time() - a
        return f

    wrapper.calls = 0
    wrapper.last_time_taken = 0
    return wrapper

