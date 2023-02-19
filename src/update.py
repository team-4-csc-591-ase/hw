import random

from src.cols import Cols
from src.config import CONSTS, CONSTS_LIST


def row(data, t):
    if data["cols"]:
        data["rows"].append(t)
        for cols in [data["cols"]["x"], data["cols"]["y"]]:
            for col in cols:
                add(col, t[col.at])
    else:
        data["cols"] = Cols(t)
    return data


def add(col, x, n=1):
    if x != "?":
        col.n = col.n + n  # Source of variable 'n'
        if col.isSym:
            col.has[x] = n + col.has.get(x, 0)
            if col.has[x] > col.most:
                col.most, col.mode = col.has[x], x
        else:
            col.lo = min(x, col.lo)
            col.hi = max(x, col.hi)
            all = len(col.has)
            if all < CONSTS_LIST[CONSTS.Max.name]:
                pos = all + 1
            elif random.random() < CONSTS_LIST[CONSTS.Max.name] / col.n:
                pos = random.randint(1, all)
            else:
                pos = None
            if pos:
                col.has[pos - 1] = x
                col.ok = False


def extend(range, n, s):
    range.lo = min(n, range.lo)
    range.hi = max(n, range.hi)
    add(range.y, s)


def adds(col, t):
    if t is None:
        return col
    for x in t:
        add(col, x)
    return col