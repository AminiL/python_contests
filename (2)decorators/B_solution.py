import functools
import queue
import json

def cache(sz):

    def decorator(func):
        q = queue.Queue(sz) #очередь для args
        d = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if sz == 0:
                return func(*args, **kwargs)
            f = 0
            zhopa = json.dumps((args, sorted(kwargs)))
            x = d.get(zhopa)
            if x is None:
                f = func(*args, **kwargs)
                if q.qsize() == sz:
                    d.pop(q.get_nowait())
                q.put(zhopa)    
                d[zhopa] = f
                return f
            else:
                return x
        return wrapper

    return decorator
