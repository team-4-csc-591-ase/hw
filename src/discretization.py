import math
from copy import deepcopy

from src.col import Col
from src.config import CONSTS, CONSTS_LIST
from src.query import div
from src.range import RANGE
from src.update import add, extend


def bins(cols, rowss):
    """

    Args:
        cols:
        rowss:

    Returns:

    """

    out = []
    for col in cols:
        ranges = {}
        for y, rows in rowss.items():
            for row in rows:
                if isinstance(col, Col):
                    col = col.col
                x = row[col.at]
                if x != "?":
                    k = int(bin(col, float(x) if x != "?" else x))
                    ranges[k] = (
                        ranges[k]
                        if k in ranges
                        else RANGE(col.at, col.txt, float(x) if x != "?" else x)
                    )
                    extend(ranges[k], float(x), y)
        ranges = {
            key: value for key, value in sorted(ranges.items(), key=lambda x: x[1].lo)
        }
        newRanges = {}
        i = 0
        for key in ranges:
            newRanges[i] = ranges[key]
            i += 1
        newRangesList = []
        if hasattr(col, "isSym") and col.isSym:
            for item in newRanges.values():
                newRangesList.append(item)
        out.append(
            newRangesList
            if hasattr(col, "isSym") and col.isSym
            else merge_any(newRanges)
        )
    return out


def bin(col, x):
    """

    Args:
        col:
        x:

    Returns:

    """
    if x == "?" or col.isSym:
        return x
    tmp = (col.hi - col.lo) / (CONSTS_LIST[CONSTS.bins.name] - 1)
    return 1 if col.hi == col.lo else math.floor((x) / tmp + 0.5) * tmp


def merge_any(ranges0):
    """

    Args:
        ranges0:

    Returns:

    """

    def no_gaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j - 1].hi
        t[0].lo = -float("inf")
        t[-1].hi = float("inf")
        return t

    ranges1, j = [], 0
    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j + 1] if j + 1 < len(ranges0) else None
        if right:
            y = merge2(left.y, right.y)
            if y:
                j = j + 1
                left.hi, left.y = right.hi, y
        ranges1.append(left)
        j += 1
    return no_gaps(ranges0) if len(ranges1) == len(ranges0) else merge_any(ranges1)


def merge2(col1, col2, n_small=None, n_far=None):
    """

    Args:
        n_far:
        n_small:
        col1:
        col2:

    Returns:

    """
    new = merge(col1, col2)
    if div(new) <= (div(col1) * col1.n + div(col2) * col2.n) / new.n:
        return new


def merge(col1, col2):
    """

    Args:
        col1:
        col2:

    Returns:

    """
    new = deepcopy(col1)
    if hasattr(col1, "isSym") and col1.isSym:
        for x, n in col2.has.items():
            add(new, x, n)
    else:
        for n in col2.has:
            add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new
