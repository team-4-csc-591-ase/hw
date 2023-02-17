import math

from src.config import CONSTS, CONSTS_LIST
from src.lists import copy
from src.query import div
from src.range import RANGE
from src.update import add, extend
from src.utils import itself


def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = []
        for y, rows in enumerate(rowss):
            for row in rows:
                x, k = row[col.at]
                if x != "?":
                    k = bin(col, x)
                    ranges[k] = ranges[k] if ranges[k] else RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
        ranges = sorted(map(ranges, itself))
        out.append(ranges if col.isSym else merge_any(ranges))
    return out


def bin(col, x):
    if x == "?" or col.isSym:
        return x
    tmp = (col.hi - col.lo) / (CONSTS_LIST[CONSTS.bins.name] - 1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + 0.5) * tmp


def merge_any(ranges0):
    def no_gaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j - 1].hi
        t[0].lo = -math.inf
        t[-1].hi = math.inf
        return t

    ranges1, j = [], 0
    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j + 1]
        if right:
            y = merge2(left.y, right.y)
            if y:
                j += 1  # next round, skip over right.
                left.hi, left.y = right.hi, y
        ranges1.append(left)
        j += 1
    return no_gaps(ranges0) if len(ranges0) == len(ranges1) else merge_any(ranges1)


def merge2(col1, col2):
    new = merge(col1, col2)
    if div(new) <= (div(col1) * col1.n + div(col2) * col2.n) / new.n:
        return new


def merge(col1, col2):
    new = copy(col1)
    if col1.isSym:
        for x, n in col2.has.items():
            add(new, x, n)
    else:
        for n in col2.has.values():
            add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new
