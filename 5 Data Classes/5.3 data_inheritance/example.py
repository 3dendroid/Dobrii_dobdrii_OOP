# class GoodMethodFactory:
#     @staticmethod
#     def get_init_measure():
#         return [0, 0, 0]
#
#
# @dataclass
# class Goods:
#     current_uid = 0
#
#     uid: int = field(init=False)
#     price: Any
#     weight: Any
#
#     def __post_init__(self):
#         print("Goods: post init")
#         Goods.current_uid += 1
#         self.uid = Goods.current_uid
#
#
# @dataclass
# class Book(Goods):
#     title: str = ""
#     author: str = ""
#     price: float = 0
#     weight: int | float = 0
#     measure: list = field(default_factory=GoodMethodFactory.get_init_measure)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print("Book: post init")
#
#
# b = Book(1000, 100, "Python", "Sazonov D.A.")
# print(b)

from dataclasses import make_dataclass, field


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass("CarData", [("model", str),
                                     "max_speed",
                                     ("price", float, field(default=0))],
                         namespace={"get_max_speed": lambda self: self.get_max_speed})

c = CarData("BMW", 256, 4999)
print(c)
print(c.get_max_speed())
