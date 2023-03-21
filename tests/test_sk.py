from src.utils import RX, gaussian, scottKnot, tiles


def test_sk():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for _ in range(1, 1000 + 1):
        a.append(gaussian(10, 1))
    for _ in range(1, 1000 + 1):
        b.append(gaussian(10.1, 1))
    for _ in range(1, 1000 + 1):
        c.append(gaussian(20, 1))
    for _ in range(1, 1000 + 1):
        d.append(gaussian(30, 1))
    for _ in range(1, 1000 + 1):
        e.append(gaussian(30.1, 1))
    for _ in range(1, 1000 + 1):
        f.append(gaussian(10, 1))
    for _ in range(1, 1000 + 1):
        g.append(gaussian(10, 1))
    for _ in range(1, 1000 + 1):
        h.append(gaussian(40, 1))
    for _ in range(1, 1000 + 1):
        j.append(gaussian(40, 3))
    for _ in range(1, 1000 + 1):
        k.append(gaussian(10, 1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v, "rx" + str(k + 1)))
    for rx in tiles(scottKnot(rxs)):
        print("", rx["rank"], rx["name"], rx["show"])
