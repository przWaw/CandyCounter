from enum import Enum


class Colors(Enum):
    RED = {
        "hLow": 170,
        "hHigh": 179,
        "sLow": 125,
        "sHigh": 255,
        "vLow": 125,
        "vHigh": 255,
        "scale": 1.9845995078193222e-05
    }
    GREEN = {
        "hLow": 35,
        "hHigh": 135,
        "sLow": 80,
        "sHigh": 255,
        "vLow": 175,
        "vHigh": 255,
        "scale": 0.00001
    }
    YELLOW = {
        "hLow": 0,
        "hHigh": 34,
        "sLow": 208,
        "sHigh": 255,
        "vLow": 132,
        "vHigh": 255,
        "scale": 5.374899220639613e-05
    }
    VIOLET = {
        "hLow": 60,
        "hHigh": 170,
        "sLow": 111,
        "sHigh": 165,
        "vLow": 0,
        "vHigh": 174,
        "scale": 4.299965600275198e-05
    }
