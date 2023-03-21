from src.num import Num


def test_num():
    n = Num()
    for i in range(1, 10 + 1):
        n.add(i)
    print("", n.n, n.mu, n.sd)
