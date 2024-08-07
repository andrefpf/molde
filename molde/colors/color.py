from PyQt5.QtGui import QColor
import numpy as np

class Color:
    color_names = {
    # Azul
    "blue100": "#FFFFFF",
    "blue90": "#ECF0FF",
    "blue80": "#C5D4FF",
    "blue70": "#84AAFF",
    "blue60": "#498FFF",
    "blue50": "#007AF0",
    "blue40": "#0069D0",
    "blue30": "#0051A2",
    "blue20": "#003A79",
    "blue10": "#002451",

    # Cinza
    "gray100": "#FFFFFF",
    "gray90": "#F0F0F5",
    "gray80": "#D3D4DD",
    "gray70": "#AAAAB9",
    "gray60": "#8F8FA2",
    "gray50": "#7A7B8E",
    "gray40": "#696979",
    "gray30": "#515162",
    "gray20": "#3A3A47",
    "gray10": "#24252E",

    # Verde
    "green100": "#FFFFFF",
    "green90": "#E1F6DF",
    "green80": "#9DE695",
    "green70": "#54C241",
    "green60": "#40A42B",
    "green50": "#2E8E16",
    "green40": "#217B00",
    "green30": "#166000",
    "green20": "#0E4700",
    "green10": "#052D00",

    # Laranja
    "orange100": "#FFFFFF",
    "orange90": "#FFECE8",
    "orange80": "#FFC8B8",
    "orange70": "#FF8C54",
    "orange60": "#E76F00",
    "orange50": "#C85D00",
    "orange40": "#AD5000",
    "orange30": "#873D00",
    "orange20": "#642B00",
    "orange10": "#421A00",

    # Roxo
    "purple100": "#FFFFFF",
    "purple90": "#F7EDFF",
    "purple80": "#E7C8FF",
    "purple70": "#D28FFF",
    "purple60": "#C762FF",
    "purple50": "#C02BFF",
    "purple40": "#AB00E7",
    "purple30": "#8600B6",
    "purple20": "#630087",
    "purple10": "#42005B",

    # Vermelho
    "red100": "#FFFFFF",
    "red90": "#FEECED",
    "red80": "#FAC8C9",
    "red70": "#FF888B",
    "red60": "#F75B60",
    "red50": "#F02532",
    "red40": "#D01E29",
    "red30": "#A4151E",
    "red20": "#790C14",
    "red10": "#510609",

    # Turquesa
    "turquoise100": "#FFFFFF",
    "turquoise90": "#DBF6F2",
    "turquoise80": "#9BE1D8",
    "turquoise70": "#50BBAF",
    "turquoise60": "#36A094",
    "turquoise50": "#1E8B7F",
    "turquoise40": "#02786D",
    "turquoise30": "#005E55",
    "turquoise20": "#00443D",
    "turquoise10": "#002B26",

    # Amarelo
    "yellow100": "#FFFFFF",
    "yellow90": "#FFEED6",
    "yellow80": "#FCCE74",
    "yellow70": "#D5A400",
    "yellow60": "#B58B00",
    "yellow50": "#9B7700",
    "yellow40": "#866600",
    "yellow30": "#684F00",
    "yellow20": "#4C3900",
    "yellow10": "#312400",

    # Rosa
    "pink100": "#FFFFFF",
    "pink90": "#FEECF1",
    "pink80": "#FBC7D5",
    "pink70": "#F888AE",
    "pink60": "#F65495",
    "pink50": "#E62881",
    "pink40": "#C8206F",
    "pink30": "#9D1756",
    "pink20": "#74103E",
    "pink10": "#4E0627",
}
 
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @classmethod
    def from_name(cls, name: str):
        if name in cls.color_names:
            hex_color = cls.color_names[name]
            return cls.from_hex(hex_color)
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


    @classmethod
    def from_qcolor(cls, color: QColor):
        return cls(color.red(), color.green(), color.blue(), color.alpha())

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

    def to_qt(self) -> QColor:
        return QColor(self.r, self.g, self.b, self.a)

