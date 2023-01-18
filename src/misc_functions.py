# convert t to a string. sort named keys.
def o(t):
    """

    Args:
        t:

    Returns:

    """
    if not (type(t).__name__ == "dict" or type(t).__name__ == "list"):
        return str(t)

    result = "{"
    keys = list(t.keys())
    keys.sort()
    for key in keys:
        result += " :" + key + " " + t[key]

    result += "}"
    return result


# print t then return it
def oo(t):
    """

    Args:
        t:

    Returns:

    """
    print(o(t))
    return t
