class StringException(Exception):
    """Базовое исключение для строк"""

class NegativeLengthString(StringException):
    """Ошибка: длина отрицательная"""

class ExceedLengthString(StringException):
    """Ошибка: длина превышает заданное значение"""

try:
    raise ExceedLengthString("длина превышает заданное значение")
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")