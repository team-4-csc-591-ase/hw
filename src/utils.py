import math
import re
from pathlib import Path
from typing import Any, cast

from src import lists
from src.config import CONSTS, CONSTS_LIST


def get_project_root() -> str:
    """
    Get absolute path of the project
    Returns: Path in string format

    """
    return str(Path(__file__).parent.parent)


def o(t):
    """

    Args:
        t:

    Returns:

    """
    if type(t) != dict and type(t) != list:
        return str(t)

    def fun(k, v):
        if str(k).find("_") != 0:
            v = o(v)
            return ":" + str(k) + " " + o(v)

        else:
            return False

    array = []
    if type(t) == dict:
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
    elif type(t) == list:
        array = t
    return "{" + " ".join(str(val) for val in array) + "}"


def oo(t: dict) -> dict:
    """

    Args:
        t: dict

    Returns: dict

    """
    print(o(t))
    return t


def settings(s: str) -> dict:
    """

    Args:
        s: String to be parsed

    Returns: Dictionary of options from parsed string

    """
    return dict(re.findall(r"\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))


def rand(lo=None, hi=None) -> float:
    """
    Args: hi, lo

    Return : float
    """
    lo, hi = lo or 0, hi or 1
    seed: int = cast(int, CONSTS_LIST[CONSTS.seed.name])
    seed = (16807 * seed) % 2147483647
    return lo + (hi - lo) * seed / 2147483647


def rnd(n, n_places=3) -> float:
    """
    Args: n, n_places = 3

    Return : float
    """
    mult = pow(10, n_places)
    return math.floor(n * mult + 0.5) / mult


def coerce(s: str) -> Any:
    """

    Args:
        s:

    Returns:

    """

    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1

    if s.isdigit():
        return int(s)
    else:
        if s.replace(".", "", 1).isdigit():
            return float(s)
        else:
            return fun(s.strip())


def cosine(a, b, c):
    """

    Args:
        a:
        b:
        c:

    Returns:

    """
    den = 1 if c == 0 else 2 * c
    x1 = (a**2 + c**2 - b**2) / den
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2)) ** 0.5
    return x2, y


def rint(lo, hi):
    """

    Args:
        lo:
        hi:

    Returns:

    """
    return math.floor(0.5 + rand(lo, hi))


def lt(x):
    """

    Args:
        x:

    Returns:

    """

    def fun(a, b):
        return a[x] < b[x]


def map(t, fun):
    """

    Args:
        t:
        fun:

    Returns:

    """
    u = []
    for k, v in enumerate(t):
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def itself(x):
    """

    Args:
        x:

    Returns:

    """
    return x


def cliffs_delta(ns1, ns2):
    """

    Args:
        ns1:
        ns2:

    Returns:

    """
    if len(ns1) > 256:
        ns1 = lists.many(ns1, 256)
    if len(ns2) > 256:
        ns2 = lists.many(ns2, 256)
    if len(ns1) > 10 * len(ns2):
        ns1 = lists.many(ns1, 10 * len(ns2))
    if len(ns2) > 10 * len(ns1):
        ns2 = lists.many(ns2, 10 * len(ns1))

    n, g_t, l_t = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y:
                g_t += 1
            if x < y:
                l_t += 1

    return abs(l_t - g_t) / n > CONSTS_LIST[CONSTS.cliffs.name]


def diffs(nums1, nums2):
    """

    Args:
        nums1:
        nums2:

    Returns:

    """

    def kap(nums, fn):
        return [fn(k, v) for k, v in enumerate(nums)]

    return kap(
        nums1,
        lambda k, nums: (cliffs_delta(nums.col.has, nums2[k].col.has), nums.col.txt),
    )


def cells(s):
    """

    Args:
        s:

    Returns:

    """
    t = []
    for s1 in s.split(","):
        t.append(coerce(s1.strip()))
    return t


def lines(file_name, fun):
    """

    Args:
        file_name:
        fun:

    Returns:

    """
    with open(file_name, "r") as src:
        for line in src:
            fun(line.rstrip("\r\n"))


def csv(file_name, fun):
    """

    Args:
        file_name:
        fun:

    Returns:

    """
    lines(file_name, lambda line: fun(cells(line)))
