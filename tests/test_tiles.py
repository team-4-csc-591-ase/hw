from src.utils import RX, gaussian, rxs_sort, tiles


def test_tiles():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    create_loop(a, 10, 1)
    create_loop(b, 10.1, 1)
    create_loop(c, 20, 1)
    create_loop(d, 30, 1)
    create_loop(e, 30.1, 1)
    create_loop(f, 10, 1)
    create_loop(g, 10, 1)
    create_loop(h, 40, 1)
    create_loop(j, 40, 3)
    create_loop(k, 10, 1)
    # for _ in range(1, 1000 + 1):
    #     a.append(gaussian(10, 1))
    # for _ in range(1, 1000 + 1):
    #     b.append(gaussian(10.1, 1))
    # for _ in range(1, 1000 + 1):
    #     c.append(gaussian(20, 1))
    # for _ in range(1, 1000 + 1):
    #     d.append(gaussian(30, 1))
    # for _ in range(1, 1000 + 1):
    #     e.append(gaussian(30.1, 1))
    # for _ in range(1, 1000 + 1):
    #     f.append(gaussian(10, 1))
    # for _ in range(1, 1000 + 1):
    #     g.append(gaussian(10, 1))
    # for _ in range(1, 1000 + 1):
    #     h.append(gaussian(40, 1))
    # for _ in range(1, 1000 + 1):
    #     j.append(gaussian(40, 3))
    # for _ in range(1, 1000 + 1):
    #     k.append(gaussian(10, 1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v, "rx" + str(k + 1)))
    rxs = rxs_sort(rxs)
    for rx in tiles(rxs):
        print("", rx["name"], rx["show"])


def create_loop(x, val, val1):
    for _ in range(1, 1000 + 1):
        x.append(gaussian(val, val1))
