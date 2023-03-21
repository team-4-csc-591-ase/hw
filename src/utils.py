import math
import random
import re
from pathlib import Path
from typing import Any, cast

from src import lists
from src.config import CONSTS, CONSTS_LIST
from src.num import Num


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


def erf(x):
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    if x < 0:
        sign = -1
    else:
        sign = 1
    x = abs(x)
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)
    return sign * y


def gaussian(mu, sd):
    mu = mu or 0
    sd = sd or 1
    sq = math.sqrt
    pi = math.pi
    log = math.log
    cos = math.cos
    r = random.random
    return mu + sd * sq(-2 * log(r())) * cos(2 * pi * r())


def samples(t, n=None):
    u = {}
    for i in range(1, (n or len(t)) + 1):
        u[i] = t[random.randint(0, len(t) - 1)]
    return u


def cliffsDelta(ns1, ns2):
    """
    Return `True` if the absolute difference between the non-parametric effect sizes
    of `ns1` and `ns2` is trivial; otherwise return `False`.
    """
    n, gt, lt = 0, 0, 0
    if len(ns1) > 128:
        ns1 = samples(ns1, 128)
    if len(ns2) > 128:
        ns2 = samples(ns2, 128)
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y:
                gt += 1
            if x < y:
                lt += 1
    return abs(lt - gt) / n <= CONSTS_LIST[CONSTS.cliff.name]


# def add(self, x):
#     self.n += 1
#     d = x - self.mu
#     self.mu = self.mu + d / self.n
#     self.m2 = self.m2 + d * (x - self.mu)
#     self.sd = 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5


def delta(self, other):
    e, y, z = 1e-32, self, other
    return abs(y.mu - z.mu) / ((e + y.sd**2 / y.n + z.sd**2 / z.n) ** 0.5)


def bootstrap(y0, z0):
    x, y, z, yhat, zhat = Num(), Num(), Num(), [], []
    for y1 in y0:
        Num.add(x, y1)
        Num.add(y, y1)
    for z1 in z0:
        Num.add(x, z1)
        Num.add(z, z1)
    xmu, ymu, zmu = x.mu, y.mu, z.mu

    for y1 in y0:
        yhat.append(y1 - ymu + xmu)
    for z1 in z0:
        zhat.append(z1 - zmu + xmu)

    tobs = delta(y, z)
    n = 0
    for _ in range(CONSTS_LIST[CONSTS.bootstrap.name]):

        if delta(Num(samples(yhat)), Num(samples(zhat))) > tobs:
            n += 1
    return n / CONSTS_LIST[CONSTS.bootstrap.name] >= CONSTS_LIST[CONSTS.conf.name]


def RX(t, s=None):
    t = sorted(t)
    return {"name": s or "", "rank": 0, "n": len(t), "show": "", "has": t}


def mid(t):
    t = t["has"] if "has" in t else t
    n = len(t) // 2
    return (t[n] + t[n + 1]) / 2 if len(t) % 2 == 0 else t[n + 1]


def div(t):
    t = t["has"] if "has" in t else t
    return (t[int(len(t) * 9 / 10)] - t[int(len(t) * 1 / 10)]) / 2.56


def merge(rx1, rx2):
    rx3 = RX([], rx1["name"])
    rx3["has"] = rx1["has"] + rx2["has"]
    rx3["has"].sort()
    rx3["n"] = len(rx3["has"])
    return rx3


def rxs_sort(rxs):
    for i, x in enumerate(rxs):
        for j, y in enumerate(rxs):
            if mid(x) < mid(y):
                rxs[j], rxs[i] = rxs[i], rxs[j]
    return rxs


def scottKnot(rxs):
    def merges(i, j):
        out = RX([], rxs[i]["name"])
        for k in range(i, j + 1):
            out = merge(out, rxs[j])
        return out

    def same(lo, cut, hi):
        l1 = merges(lo, cut)
        r1 = merges(cut + 1, hi)
        return cliffsDelta(l1["has"], r1["has"]) and bootstrap(l1["has"], r1["has"])

    def recurse(lo, hi, rank):
        b4 = merges(lo, hi)
        best = 0
        cut = None
        for j in range(lo, hi + 1):
            if j < hi:
                l1 = merges(lo, j)
                r1 = merges(j + 1, hi)
                now = (
                    l1["n"] * (mid(l1) - mid(b4)) ** 2
                    + r1["n"] * (mid(r1) - mid(b4)) ** 2
                ) / (l1["n"] + r1["n"])
                if now > best:
                    if abs(mid(l1) - mid(r1)) >= cohen:
                        cut, best = j, now
        if cut is not None and not same(lo, cut, hi):
            rank = recurse(lo, cut, rank) + 1
            rank = recurse(cut + 1, hi, rank)
        else:
            for i in range(lo, hi + 1):
                rxs[i]["rank"] = rank
        return rank

    rxs = sorted(rxs, key=lambda x: mid(x))
    cohen = div(merges(0, len(rxs) - 1)) * CONSTS_LIST[CONSTS.cohen.name]
    recurse(0, len(rxs) - 1, 1)
    return rxs


# def tiles(rxs):
#     huge = math.inf
#     lo, hi = huge, -huge
#     for rx in rxs:
#         lo, hi = min(lo, rx["has"][0]), max(hi, rx["has"][-1])
#     for rx in rxs:
#         t, u = rx["has"], []
#
#         def of(x, most):
#             return max(1, min(most, x))
#
#         def at(x):
#             return t[of(len(t) * x // 1, len(t) - 1)]
#
#         def pos(x):
#             return math.floor(
#                 of(
#                     CONSTS_LIST[CONSTS.width.name] *(x - lo) / (hi - lo + 1e-32) // 1,
#                     CONSTS_LIST[CONSTS.width.name],
#                 )
#             )
#
#         for i in range(CONSTS_LIST[CONSTS.width.name]):
#             u.append(" ")
#         a, b, c, d, e = at(0.1), at(0.3), at(0.5), at(0.7), at(0.9)
#         A, B, C, D, E = pos(a), pos(b), pos(c), pos(d), pos(e)
#         for i in range(A, B + 1):
#             u[i] = "-"
#         for i in range(D, E + 1):
#             u[i] = "-"
#         u[CONSTS_LIST[CONSTS.width.name] // 2] = "|"
#         u[C] = "*"
#         rx.show = "".join(u) + " {" + f"{a:.2f}"
#         for x in [b, c, d, e]:
#             rx.show += f", {x:.2f}"
#         rx.show += "}"
#     return rxs
def tiles(rxs):
    huge = float("inf")
    lo, hi = huge, float("-inf")
    for rx in rxs:
        lo, hi = min(lo, rx["has"][0]), max(hi, rx["has"][len(rx["has"]) - 1])
    for rx in rxs:
        t, u = rx["has"], []

        def of(x, most):
            return int(max(0, min(most, x)))

        def at(x):
            return t[of(len(t) * x // 1, len(t))]

        def pos(x):
            return math.floor(
                of(
                    CONSTS_LIST[CONSTS.width.name] * (x - lo) / (hi - lo + 1e-32) // 1,
                    CONSTS_LIST[CONSTS.width.name],
                )
            )

        for i in range(0, CONSTS_LIST[CONSTS.width.name] + 1):
            u.append(" ")
        a, b, c, d, e = at(0.1), at(0.3), at(0.5), at(0.7), at(0.9)
        A, B, C, D, E = pos(a), pos(b), pos(c), pos(d), pos(e)
        for i in range(A, B + 1):
            u[i] = "-"
        for i in range(D, E + 1):
            u[i] = "-"
        u[CONSTS_LIST[CONSTS.width.name] // 2] = "|"
        u[C] = "*"
        x = []
        for i in [a, b, c, d, e]:
            x.append("{:.2f}".format(i))
        rx["show"] = "".join(u) + str(x)
    return rxs
