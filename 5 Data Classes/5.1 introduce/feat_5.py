from dataclasses import dataclass


@dataclass
class House:
    addr: str
    size: float
    floors: int = 1
    rooms: int = 3

    def __eq__(self, other):
        return self.floors == other.floors and self.rooms == other.rooms


h1 = House("Москва, ул. Тверская, д. 5", 102.5, 3, 7)
h2 = House("Москва, ул. Воздвиженка, д. 11", 82.3, 2, 6)
