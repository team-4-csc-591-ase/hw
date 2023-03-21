from src.num import Num
from src.utils import gaussian


def test_gauss():
    t = []
    for i in range(1, 10**4 + 1):
        t.append(gaussian(10, 2))
    n = Num()
    for i in t:
        n.add(i)
    print("", n.n, n.mu, n.sd)
