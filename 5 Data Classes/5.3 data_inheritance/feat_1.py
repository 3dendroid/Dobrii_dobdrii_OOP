from dataclasses import dataclass, field

@dataclass
class Geom:
    color_line: int
    color_bg: int


@dataclass
class Line(Geom):
    sp: tuple = field(default_factory=tuple)
    ep: tuple = field(default_factory=tuple)

    def __post_init__(self):
        x0, y0 = self.sp[0], self.sp[1]
        x1, y1 = self.ep[0], self.ep[1]
        self.length = ((x0-x1) * (x0-x1) + (y0-y1) * (y0-y1)) ** 0.5

line = Line(0, 0, (-5, 7), (10, 20))