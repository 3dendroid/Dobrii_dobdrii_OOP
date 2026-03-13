from dataclasses import dataclass

@dataclass
class TableCircle:
    model: str
    price: float
    height: int
    radius: int

    def __eq__(self, other):
        return (self.height, self.radius) == (other.height, other.radius)


t1 = TableCircle("Python Table", 80001, 900, 300)
t2 = TableCircle("Table Python", 80002, 900, 300)

res = t1 == t2
print(t1)
print(t2)
print(res)
