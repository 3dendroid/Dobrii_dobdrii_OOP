class CellException(Exception):
    """Базовое исключение для ячеек"""

class CellIntegerException(CellException):
    pass

class CellFloatException(CellException):
    pass

class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, int) or isinstance(val, bool) or not (self._min_value <= val <= self._max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = val


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, (int, float)) or isinstance(val, bool) or not (self._min_value <= val <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = val


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str) or not (self._min_length <= len(val) <= self._max_length):
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = val


class TupleData:
    def __init__(self, *args):
        self._data = args

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._data):
            raise IndexError('индекс выходит за допустимый диапазон')
        return self._data[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0 or index >= len(self._data):
            raise IndexError('индекс выходит за допустимый диапазон')
        self._data[index].value = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")