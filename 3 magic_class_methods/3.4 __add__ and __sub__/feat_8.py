class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if not isinstance(other, Item) and not isinstance(other.money, (int, float)):
            raise AttributeError("Неправильный тип данных")
        self.money += other.money
        return self.money

    def __radd__(self, other):
        return other + self.money


class Budget:
    lst_it = []

    def add_item(self, it):
        self.lst_it.append(it.money)

    def remove_item(self, indx):
        del self.lst_it[indx]

    def get_items(self):
        return self.lst_it
