class Vector:
    def __init__(self, *coords):
        # coords: кортеж из числовых координат
        self._coords = list(coords)

    def _check_dims(self, other):
        if len(self._coords) != len(other._coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self._check_dims(other)
        return Vector(*(a + b for a, b in zip(self._coords, other._coords)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self._check_dims(other)
        return Vector(*(a - b for a, b in zip(self._coords, other._coords)))

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self._check_dims(other)
        return Vector(*(a * b for a, b in zip(self._coords, other._coords)))

    def __iadd__(self, other):
        # прибавление в-месте: либо число, либо вектор
        if isinstance(other, Vector):
            self._check_dims(other)
            for i in range(len(self._coords)):
                self._coords[i] += other._coords[i]
        elif isinstance(other, (int, float)):
            for i in range(len(self._coords)):
                self._coords[i] += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other):
        # вычитание в-месте: либо число, либо вектор
        if isinstance(other, Vector):
            self._check_dims(other)
            for i in range(len(self._coords)):
                self._coords[i] -= other._coords[i]
        elif isinstance(other, (int, float)):
            for i in range(len(self._coords)):
                self._coords[i] -= other
        else:
            return NotImplemented
        return self

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self._coords) != len(other._coords):
            return False
        return all(a == b for a, b in zip(self._coords, other._coords))

    def __ne__(self, other):
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    def __repr__(self):
        return f"Vector({', '.join(map(str, self._coords))})"
