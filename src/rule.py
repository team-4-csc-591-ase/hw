from src.utils import prune


class Rule:
    def __init__(self, ranges, maxSize):
        t = {}
        for range in ranges:
            t[range.txt] = t.get(range.txt, [])
            t[range.txt].append({"lo": range.lo, "hi": range.hi, "at": range.at})
        prune(t, maxSize)
