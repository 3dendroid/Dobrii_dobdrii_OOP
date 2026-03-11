class Tuple(tuple):
    def __add__(self, other):
        if isinstance(other, (list, tuple, str, set, dict)):
            # превращаем итерируемый объект в tuple и создаем новый объект Tuple
            return Tuple(tuple(self) + tuple(other))
        # если объект не итерируемый, выбрасываем исключение
        raise TypeError("Right operand must be iterable")
