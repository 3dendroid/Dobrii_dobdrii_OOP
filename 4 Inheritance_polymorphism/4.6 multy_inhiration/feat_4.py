class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value
        super().__init__()


class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        if value < 2:
            raise TypeError('значение не соответствует типу объекта')

        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                raise TypeError('значение не соответствует типу объекта')

        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


# создаём объекты
digits = [
    PrimeNumber(2),
    PrimeNumber(3),
    PrimeNumber(11),

    FloatPositive(1.5),
    FloatPositive(2.3),
    FloatPositive(10.0),
    FloatPositive(0.25),
    FloatPositive(7.8)
]

# списки по условию
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))





