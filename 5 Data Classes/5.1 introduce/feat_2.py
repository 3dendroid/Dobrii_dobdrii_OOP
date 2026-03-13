from dataclasses import dataclass

@dataclass
class Car:
    model: str
    price: float
    dist: int = 0


car1 = Car('BMW X6', 1200)
car2 = Car('BMW X5', 1000, 100)

print(car1)
print(car2)
print(car1 == car2)