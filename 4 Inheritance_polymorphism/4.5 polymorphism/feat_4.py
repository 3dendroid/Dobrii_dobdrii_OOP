class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __counter = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price

        ShopItem.__counter += 1
        self.__id = ShopItem.__counter

    def get_id(self):
        return self.__id





