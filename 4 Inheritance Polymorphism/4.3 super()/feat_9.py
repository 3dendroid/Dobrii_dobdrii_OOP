class StringDigit(str):
    def __new__(cls, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return super().__new__(cls, string)

    def __add__(self, other):
        new_str = super().__str__() + str(other)
        if not new_str.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(new_str)

    def __radd__(self, other):
        new_str = str(other) + super().__str__()
        if not new_str.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(new_str)
