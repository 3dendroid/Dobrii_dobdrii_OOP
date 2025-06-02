import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        if not isinstance(other, ShopItem):
            return NotImplemented
        return (self.name.lower(), self.weight, self.price) == (
            other.name.lower(), other.weight, other.price
        )


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!

# словарь: ключ = объект ShopItem, значение = [ShopItem, total]
shop_items = {}

for line in lst_in:

    name_part, rest = line.split(':', 1)
    name = name_part.strip()
    weight_str, price_str = rest.strip().split()
    weight = float(weight_str)
    price = float(price_str)

    item = ShopItem(name, weight, price)

    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, 1]
