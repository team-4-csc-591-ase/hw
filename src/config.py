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
}
