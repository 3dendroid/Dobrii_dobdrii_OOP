class PositiveValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = PositiveValue()
    b = PositiveValue()
    c = PositiveValue()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle__(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle__(value, self.b, self.c)) or \
                (key == 'b' and not self.__is_triangle__(self.a, value, self.c)) or \
                (key == 'c' and not self.__is_triangle__(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c) if self.a and self.b and self.c else None

    def __call__(self):
        a, b, c = self.a, self.b, self.c
        if not (a and b and c):
            return
        p = 0.5 * (a + b + c)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
