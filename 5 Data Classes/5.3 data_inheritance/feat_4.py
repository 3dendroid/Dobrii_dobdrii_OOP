from dataclasses import dataclass, field
from typing import Any
from dataclasses import InitVar


@dataclass
class Table:
    current_id = 0
    id: int = field(init=False, compare=False, default=-1)
    model: str
    color: Any

    def __post_init__(self):
        Table.current_id += 1
        self.id = Table.current_id


@dataclass
class RoundTable(Table):
    radius: InitVar[int]
    height: int
    square: float = field(init=False, compare=False, default=0.0)

    def __post_init__(self, radius):
        super().__post_init__()
        self.square = 3.1415 * radius ** 2


rt = RoundTable(model="RT", color="green", radius=120, height=90)