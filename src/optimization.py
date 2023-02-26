from src import query
from src.clustering import half
from src.config import CONSTS, CONSTS_LIST


def sway(data):
    """

    Args:
        data:

    Returns:

    """

    def worker(rows, worse, above=None):
        """

        Args:
            rows:
            worse:
            above:

        Returns:

        """
        if len(rows) <= len(data.rows) ** CONSTS_LIST[CONSTS.min.name]:
            return rows, lists.many(worse, CONSTS_LIST[CONSTS.rest.name] * len(rows))
        else:
            l, r, A, B, _ = half(data, rows, None, above)
            if query.better(data, B, A):
                l, r, A, B = r, l, B, A
            for row in r:
                worse.append(row)
            # map(r, lambda row: worse.append(row))
            return worker(l, worse, A)

    best, rest = worker(data.rows, [])
    return data.clone(data, best), data.clone(data, rest)
