import random
from dataclasses import dataclass, field
from typing import Any


class GlobalGraphData:
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'gray']

    @staticmethod
    def get_color():
        return GlobalGraphData.colors[random.randint(0, len(GlobalGraphData.colors)-1)]


@dataclass
class Graph:
    width: float = field(default=0.5, init=False, compare=False)
    color: Any = field(default_factory=GlobalGraphData.get_color, init=False, compare=False)


@dataclass
class Rect(Graph):
    sp: tuple = field(default_factory=tuple)
    ep: tuple = field(default_factory=tuple)

    def draw(self):
        return f"Rect: {self.sp}; {self.ep}"


rect = Rect(sp=(1, 2), ep=(10, 20))