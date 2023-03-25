import math
import random


def push(t, x):
    """
    Push an item `x` onto a list.
    Args:
        t:
        x:

    Returns:

    """
    t.append(x)
    return x


def sort(t, f):
    """
    Return a list, sorted on `fun`.
    Args:
        t:
        f:

    Returns:

    """
    return sorted(t, key=f)


def lt(x):
    """
    Return a function sorting down on field `x`.
    Args:
        x:

    Returns:

    """
    return lambda a, b: a[x] < b[x]


def gt(x):
    """
    Return a function sorting up on field `x`.
    Args:
        x:

    Returns:

    """
    return lambda a, b: a[x] > b[x]


def any(t):
    """
    Return one item at random
    Args:
        t:

    Returns:

    """
    return random.choice(t)


def many(t, n):
    """
    Return many items, selected at random.
    Args:
        t:
        n:

    Returns:

    """
    u = []
    for i in range(1, n + 1):
        u.append(any(t))
    return u


def map(t, fun):
    """
    Map a function on table (results in items 1,2,3...)
    Args:
        t:
        fun:

    Returns:

    """
    u = {}
    for i, v in enumerate(t):
        u[i + 1] = fun(v)
    return u


def kap(t, fun):
    """
    Map a function on table (results in items key1,key2,...)
    Args:
        t:
        fun:

    Returns:

    """
    u = {}
    if isinstance(t, list):
        e = enumerate(t)
    else:
        e = t.items()

    for k, v in enumerate(e):
        v, k = fun(k, v)
        u[k or len(u) + 1] = v
    return u


def per(t, p=0.5):
    """
    Return the `p`-ratio item in `t`; e.g. `per(t,.5)` returns the medium.
    Args:
        t:
        p:

    Returns:

    """
    p = math.floor(((p or 0.5) * len(t) - 1) + 0.5)
    return t[max(1, min(len(t) - 1, p))]
    # p=math.floor(((p or .5)*#t)+.5);
    # # return t[m.max(1,m.min(#t,p))]


def copy(t):
    """
    Deep copy of a table `t`.
    Args:
        t:

    Returns:

    """
    if type(t) is not dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u


def slice(t, go=None, stop=None, inc=None):
    """
    Return a portion of `t`; go,stop,inc defaults to 1,#t,1.
    Negative indexes are supported.
    Args:
        t:
        go:
        stop:
        inc:

    Returns:

    """
    if go and go < 0:
        go = len(t) + go
    if stop and stop < 0:
        stop = len(t) + stop
    u = []
    for j in range(go or 0, stop or len(t), inc or 1):
        u.append(t[j])
    return u
