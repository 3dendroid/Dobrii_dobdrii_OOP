from dataclasses import dataclass, field

@dataclass
class PolyLine:
    width: float
    color: int
    points: list = field(default_factory=list)

    def __post_init__(self):
        if len(self.points) < 2:
            self.length = 0
            return

        x0, y0 = self.points[0]
        x1, y1 = self.points[-1]
        self.length = ((x1-x0) * (x1-x0) + (y1-y0) * (y1-y0)) ** 0.5


pl = PolyLine(0.5, 0)
pl.points.extend([(10, -5), (12, 1), (40, -18)])
print(pl)