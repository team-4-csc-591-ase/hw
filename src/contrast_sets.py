from src.discretization import bins
from src.lists import kap
from src.query import value
from src.rule import Rule
from src.utils import o, oo, rnd


def xpln(data, best, rest):
    def v(has):
        return value(has, len(best.rows), len(rest.rows), "best")

    def score(ranges):
        rule = Rule(ranges, max_sizes)
        if rule:
            oo(show_rule(rule))
            bestr = selects(rule, best.rows)
            restr = selects(rule, rest.rows)
            if len(bestr) + len(restr) > 0:
                return v({"best": len(bestr), "rest": len(restr)}), rule

    tmp = []
    max_sizes = []
    for _, ranges in bins(data.cols.x, {"best": best.rows, "rest": rest.rows}).items():
        max_sizes[ranges[0].txt] = len(ranges)
        print("")
        for _, range in enumerate(ranges):
            print(range.txt, range.lo, range.hi)
            tmp.append({"range": range, "max": len(ranges), "val": v(range.y.has)})
    rule, most = firstN(sorted(tmp, key=lambda x: x["val"], reverse=True), score)
    return rule, most


def firstN(sorted_ranges, score_fun):
    print("")
    for r in sorted_ranges:
        print(
            r["range"].txt,
            r["range"].lo,
            r["range"].hi,
            round(r["val"], 2),
            r["range"].y.has,
        )
    first = sorted_ranges[0]["val"]

    def useful(range):
        if range["val"] > 0.05 and range["val"] > first / 10:
            return range

    sorted_ranges = list(
        filter(lambda r: useful(r), sorted_ranges)
    )  # reject  useless ranges
    most, out = -1, None
    for n in range(1, len(sorted_ranges) + 1):
        tmp, rule = score_fun(list(map(lambda r: r["range"], sorted_ranges[:n])))
        if tmp and tmp > most:
            out, most = rule, tmp
    return out, most


def show_rule(rule):
    def pretty(range):
        return range.lo if range.lo == range.hi else [range.lo, range.hi]

    def merges(attr, ranges):
        return [pretty(r) for r in merge(sorted(ranges, key=lambda r: r.lo))], attr

    def merge(t0):
        t, j = [], 0
        while j < len(t0):
            left, right = t0[j], t0[j + 1] if j + 1 < len(t0) else None
            if right and left.hi == right.lo:
                left.hi = right.hi
                j += 1
            t.append({"lo": left.lo, "hi": left.hi})
            j += 1
        return t if len(t0) == len(t) else merge(t)

    return kap(rule, merges)


def selects(rule, rows):
    def disjunction(ranges, row):
        for range in ranges:
            lo, hi, at = range.lo, range.hi, range.at
            x = row[at]
            if x == "?":
                return True
            if lo == hi == x:
                return True
            if lo <= x < hi:
                return True
        return False

    def conjunction(row):
        for ranges in rule:
            if not disjunction(ranges, row):
                return False
        return True

    return [r for r in rows if conjunction(r)]
