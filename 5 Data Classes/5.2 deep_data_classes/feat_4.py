from dataclasses import dataclass, field


@dataclass
class Velocity:
    model: str = field(compare=False)
    speed: float = field(init=False, default=0)
    weight: float = field()
    dims: tuple = field(compare=False, repr=False, default=None)


vl1 = Velocity(model="car", weight=5.4, dims=(100, 20, 30))
vl2 = Velocity(model="ship", weight=5.4, dims=(500, 200, 130))

res = vl1 == vl2