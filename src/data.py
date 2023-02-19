from src.utils import csv
from src.update import row


def new():
    """

    Returns:

    """
    return {"rows": [], "cols": None}


def read(file_name):
    """

    Args:
        file_name:

    Returns:

    """
    data = new()
    csv(file_name, lambda t: row(data, t))
    return data


def clone(data, ts=None):
    """

    Args:
        data:
        ts:

    Returns:

    """
    data1 = row(new(), data.cols.names)
    for t in ts or []:
        row(data1, t)
    return data1
