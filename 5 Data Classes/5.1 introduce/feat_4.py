from dataclasses import dataclass


@dataclass
class Person:
    fio: str
    old: int
    salary: int = 0
