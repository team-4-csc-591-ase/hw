from enum import Enum
from typing import Any, Dict


class CONSTS(Enum):
    seed = "seed"
    dump = "dump"
    go = "go"
    help = "help"
    file = "file"
    p = "p"
    Sample = "Sample"
    Far = "Far"
    min = "min"
    cliffs = "cliffs"
    bins = "bins"
    Max = "Max"
    Reuse = "Reuse"
    Halves = "Halves"
    rest = "rest"
    bootstrap = "bootstrap"
    conf = "conf"
    cliff = "cliff"
    cohen = "cohen"
    width = "width"


CONSTS_LIST: Dict[str, Any] = {
    CONSTS.seed.name: 937162211,
    CONSTS.dump.name: False,
    CONSTS.go.name: "data",
    CONSTS.help.name: False,
    CONSTS.file.name: "auto93.csv",
    CONSTS.p.name: 2,
    CONSTS.Far.name: 0.95,
    CONSTS.min.name: 0.5,
    CONSTS.Sample.name: 512,
    CONSTS.cliffs.name: 0.147,
    CONSTS.bins.name: 16,
    CONSTS.Max.name: 512,
    CONSTS.Reuse.name: True,
    CONSTS.Halves.name: 512,
    CONSTS.rest.name: 4,
    CONSTS.bootstrap.name: 512,
    CONSTS.conf.name: 0.05,
    CONSTS.cliff.name: 0.4,
    CONSTS.cohen.name: 0.35,
    CONSTS.width.name: 40,
}
