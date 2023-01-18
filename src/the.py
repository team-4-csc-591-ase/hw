import re


def o(t):
    if not (type(t).__name__ == "dict" or type(t).__name__ == "list"):
        return str(t)

    if type(t).__name__ == "list":
        p = [str(i) for i in t]
        return "{" + "".join(p) + "}"

    def show(k, v):
        if not re.search("^_", k):
            v = o(v)
            return f":{k} {v}"

    u = []
    keys = list(t.keys())
    for key in keys:
        val = show(key, t[key])
        if val:
            u.append(val)

    u.sort()
    return "{" + "".join(u) + "}"


# print t then return it
def oo(t):
    print(o(t))
    return t
