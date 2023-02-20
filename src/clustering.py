# from src.data import Data
# from src.lists import many
from src import lists, query
from src.config import CONSTS, CONSTS_LIST

# from src.query import dist, stats


# Cluster `rows` into two sets by
# dividing the data via their distance to two remote points.
# To speed up finding those remote points, only look at
# `some` of the data. Also, to avoid outliers, only look
# `the.Far=.95` (say) of the way across the space.
def half(data, rows=None, cols=None, above=None):
    def gap(r1, r2):
        return query.dist(data, r1, r2, cols)

    def cos(a, b, c):
        return (a**2 + c**2 - b**2) / (2 * c)

    def proj(r):
        return {"row": r, "x": cos(gap(r, A), gap(r, B), c)}

    rows = rows or data.rows
    some = lists.many(rows, CONSTS_LIST[CONSTS.Halves.name])
    A = above or lists.any(some)
    tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
    far = tmp[int(len(tmp) * CONSTS_LIST[CONSTS.Far.name]) // 1]
    B, c, left, right = far["row"], far["d"], [], []
    for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
        if n <= (len(rows) - 1) / 2:
            left.append(two["row"])
        else:
            right.append(two["row"])
    return left, right, A, B, c


# Cluster, recursively, some `rows` by  dividing them in two, many times
def tree(data, rows=None, cols=None, above=None):
    rows = rows or data.rows
    here = {"data": data.clone(data, rows)}
    if len(rows) >= 2 * (len(data.rows) ** CONSTS_LIST[CONSTS.min.name]):
        left, right, A, B, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)
    return here


# Cluster can be displayed by this function.
def show_tree(tree, lvl=0, post=None):
    if tree:
        print("{}[{}]".format("|.. " * lvl, len(tree["data"].rows)), end="")
        if lvl == 0 or ("left" not in tree):
            print(query.stats(tree["data"]))
        else:
            print("")
        show_tree(tree["left"] if "left" in tree else None, lvl + 1)
        show_tree(tree["right"] if "right" in tree else None, lvl + 1)
