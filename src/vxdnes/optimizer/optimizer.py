import functools

def add(a:int, b:int)->int:
    pass

def subtract(a: int, b: int)->int:
    return

from . import _optimizer
g = globals()
for key in dir(_optimizer):
    print(key)
    attr = getattr(_optimizer, key, None)
    if attr is not None:
        g[key] = attr