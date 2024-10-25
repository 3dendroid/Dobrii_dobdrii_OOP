class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append (gd)

    def remove(self, indx):
        self.goods.pop (indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart ()
cart.add (TV ('Xiaomi', 1100))
cart.add (TV ('Sony', 2000))
cart.add (Table ('Gurdgen', 1700))
cart.add (Notebook ('Gigabyte', 3000))
cart.add (Notebook ('MSI', 3500))

print (cart.get_list ())
