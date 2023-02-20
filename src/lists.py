import random


# Push an item `x` onto a list.
def push(t, x):
    t.append(x)
    return x


# Return a list, sorted on `fun`.
def sort(t, f):
    return sorted(t, key=f)


# Return a function sorting down on field `x`.
def lt(x):
    return lambda a, b: a[x] < b[x]


# Return a function sorting up on field `x`.
def gt(x):
    return lambda a, b: a[x] > b[x]


# Return one item at random.
def any(t):
    return random.choice(t)


# Return many items, selected at random.
def many(t, n):
    """

    Args:
        t:
        n:

    Returns:

    """
    u = []
    for i in range(1, n + 1):
        u.append(any(t))
    return u


# Map a function on table (results in items 1,2,3...)
def map(t, fun):
    u = {}
    for i, v in enumerate(t):
        u[i + 1] = fun(v)
    return u


# Map a function on table (results in items key1,key2,...)
def kap(t, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or len(u) + 1] = v
    return u


# Return the `p`-ratio item in `t`; e.g. `per(t,.5)` returns the medium.
def per(t, p=0.5):
    p = int(round(p * len(t)))
    return t[min(max(1, p), len(t)) - 1]


# Deep copy of a table `t`.
def copy(t):
    if type(t) is not dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u


# Return a portion of `t`; go,stop,inc defaults to 1,#t,1.
# Negative indexes are supported.
def slice(t, go=None, stop=None, inc=None):
    if go and go < 0:
        go = len(t) + go
    if stop and stop < 0:
        stop = len(t) + stop
    u = []
    for j in range(go or 0, stop or len(t), inc or 1):
        u.append(t[j])
    return u
