import math

from src.lists import per


def div(col):
    if hasattr(col, "isSym"):
        e = 0
        if isinstance(col.has, dict):
            for n in col.has.values():
                e = e - n / col.n * math.log(n / col.n, 2)
        else:
            for n in col.has:
                e = e - n / col.n * math.log(n / col.n, 2)
        return e
    else:
        return (per(has(col), 0.9) - per(has(col), 0.1)) / 2.58


def has(col):
    if not col.isSym and not col.ok:
        col.has.sort()
    col.ok = True
    return col.has
