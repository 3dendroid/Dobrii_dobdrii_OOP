class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return f'Integer({self.__value})'


class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for i in range(0, self.__max_length)]

    def __check(self, index):
        if type(index) != int or not (-self.__max_length <= index < self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.__array[item].value

    def __setitem__(self, key, value):
        self.__check(key)
        self.__array[key].value = value

    def __repr__(self):
        return f' '.join(str(cell.value) for cell in self.__array)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError