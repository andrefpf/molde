from PyQt5.QtGui import QColor
import numpy as np

class Color:
    color_names = {
        "blue10": (0, 36, 81), 
        "green70": (0, 179, 0),
        #...
    }
    
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @classmethod
    def from_name(cls, name: str):
        if name in cls.color_names:
            r, g, b = cls.color_names[name]
            return cls(r, g, b)
        raise ValueError("Unknown color name")

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int):
        r = int(np.clip(r, 0, 255))
        g = int(np.clip(g, 0, 255))
        b = int(np.clip(b, 0, 255))
        return cls(r, g, b)

    @classmethod
    def from_rgba(cls, r: int, g: int, b: int, a: int=255):
        r = int(np.clip(r, 0, 255))
        g = int(np.clip(g, 0, 255))
        b = int(np.clip(b, 0, 255))
        a = int(np.clip(a, 0, 255))
        return cls(r, g, b, a)

    @classmethod
    def from_rgb_f(cls, r: float, g: float, b: float):
        r = float(np.clip(r, 0, 1))
        g = float(np.clip(g, 0, 1))
        b = float(np.clip(b, 0, 1))
        return cls(int(r * 255), int(g * 255), int(b * 255))

    @classmethod
    def from_rgba_f(cls, r: float, g: float, b: float, a: float):
        r = float(np.clip(r, 0, 1))
        g = float(np.clip(g, 0, 1))
        b = float(np.clip(b, 0, 1))
        a = float(np.clip(a, 0, 1))
        return cls(int(r * 255), int(g * 255), int(b * 255), int(a * 255))

    @classmethod
    def from_hex(cls, color: str):
        color = color.lstrip('#')
        if len(color) == 6:
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            return cls(r, g, b)
        elif len(color) == 8:
            r, g, b, a = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16), int(color[6:8], 16)
            return cls(r, g, b, a)
        raise ValueError("Invalid hex color format")

    #@classmethod
    # def from_qcolor(cls, color: QColor):
    #     return cls(color.red(), color.green(), color.blue(), color.alpha())

    def to_rgb(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)

    def to_rgba(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

    def to_rgb_f(self) -> tuple[float, float, float]:
        return ((self.r / 255), (self.g / 255), (self.b / 255))

    def to_rgba_f(self) -> tuple[float, float, float, float]:
        return ((self.r / 255), (self.g / 255), (self.b / 255), (self.a / 255))

    def to_hex(self) -> str:
        return (f'#{self.r:02X}{self.g:02X}{self.b:02X}')

    def to_hexa(self) -> str:
        return (f'#{self.r:02X}{self.g:02X}{self.b:02X}{self.a:02X}')

    #def to_qt(self) -> QColor:
        #return QColor(self.r, self.g, self.b, self.a)


color1 = Color.from_hex("#FD0034")
print(color1.to_rgb())