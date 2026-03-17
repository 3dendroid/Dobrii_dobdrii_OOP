from dataclasses import dataclass, field


@dataclass
class Student:
    fio: str
    group: str
    marks: list = field(default_factory=list)


s1 = Student("Ганди Индира", "МГИМО-11", [5, 4, 3])
s2 = Student("Манделла Нельсон", "МГИМО-32")
