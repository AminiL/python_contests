import itertools


def transpose(lst):
    return list(zip(*lst))

def uniq(lst):
    s = set()
    return [x for x in lst if not(x in s or s.add(x))]

def dict_merge(*args):
    c = args[0].copy()
    for i in range(1, len(args)):
        c.update(args[i])
    return c

def product(a, b):
    s = 0
    A = iter(a)
    B = iter(b)
    while True:
        try:
            s += A.__next__() * B.__next__()
        except:
            break
    return s
