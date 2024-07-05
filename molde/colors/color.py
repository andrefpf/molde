from dataclasses import dataclass

import numpy as np


@dataclass
class Color:
    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255

    @classmethod
    def from_rgba(cls, r: int, g: int, b: int, a: int = 255):
        r = int(np.clip(r, 0, 255))
        g = int(np.clip(g, 0, 255))
        b = int(np.clip(b, 0, 255))
        return cls(r, g, b, a)
