from dataclasses import dataclass


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float

    # def __eq__(self, other):
    #     return self.weight == other.weight


# td = ThingData("Java Book", 100, 1024)
t = Thing("Java Book", 100, 1024)
t.dims.append(10)
print(t)
