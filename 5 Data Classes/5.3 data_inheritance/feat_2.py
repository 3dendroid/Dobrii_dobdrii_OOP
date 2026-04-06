from dataclasses import dataclass
from typing import Any


@dataclass
class Thing:
    name: Any
    color: Any
    weight: float


@dataclass
class Table(Thing):
    width: float = 0.0
    height: float = 0.0


tb = Table(name="Suprise", color="red", weight=102.5, width=0.45, height=10.1)
