from src.data import *
from src.clustering import *
from src.query import *


def sway(data):
  def worker(rows, worse, above=None):
    if len(rows) <= len(data.rows) ** CONSTS_LIST[CONSTS.min.name]:
      return rows, many(worse, CONSTS_LIST[CONSTS.rest.name]*len(rows))
    else:
      l, r, A, B = half(data, rows, None, above)
      if better(data, B, A):
        l, r, A, B = r, l, B, A
      map(r,lambda row:worse.append(row))
      return worker(l, worse, A)
  best, rest = worker(data.rows, {}, [])
  return Data.clone(data, best), Data.clone(data, rest)
