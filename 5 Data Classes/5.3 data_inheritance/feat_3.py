from dataclasses import dataclass, field
from typing import Any


@dataclass
class Animal:
    name: str
    old: int
    weight: Any


@dataclass
class Turtle(Animal):
    weight: float = 0.0
    length: float = 0.0
    speed: float = field(default=0, init=False)


t = Turtle(name="Черя", old=94, weight=3.5, length=108)