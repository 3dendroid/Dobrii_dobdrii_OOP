class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self._name, self._weight, self._tp, self._doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        if not isinstance(height, (int, float)) or height <= 0:
            raise TypeError('вес должен быть положительным числом')
        self._height = height

    def get_attrs(self):
        return self._name, self._weight, self._height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        if not isinstance(height, (int, float)) or height <= 0:
            raise TypeError('вес должен быть положительным числом')
        if not isinstance(square, (int, float)) or square <= 0:
            raise TypeError('вес должен быть положительным числом')
        self._height = height
        self._square = square

    def get_attrs(self):
        return self._name, self._weight, self._height, self._square
