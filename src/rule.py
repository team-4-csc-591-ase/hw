class Rule:
    def __init__(self, ranges, max_size):
        t = []
        for range in ranges:
            t[range.txt] = t[range.txt] or {}
            t[range.txt].append({"lo": range.lo, "hi": range.hi, "at": range.at})
        self.prune(t, max_size)

    def prune(self, rule, max_size):
        n = 0
        for txt, ranges in enumerate(rule):
            n += 1
            if len(ranges) == max_size[txt]:
                n += 1
                rule[txt] = None
        if n > 0:
            return rule
