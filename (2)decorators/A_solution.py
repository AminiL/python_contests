import functools
import sys


def takes(*args_dec):

    def decorator(func):
        sz_takes = len(args_dec)

        @functools.wraps(func)
        def wrapper(*args):
            sz_func = len(args)
            dl = min((sz_func, sz_takes))
            for i in range(dl):
                if not isinstance(args[i], args_dec[i]):
                    raise TypeError
            return func(*args)

        return wrapper

    return decorator

exec(sys.stdin.read())
