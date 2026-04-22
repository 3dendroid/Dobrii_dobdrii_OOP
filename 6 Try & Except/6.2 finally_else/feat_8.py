class Rect:
    def __init__(self, x, y, width, height):
        # Сначала инициализируем, чтобы __setattr__ мог проверить значения
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        # Проверка на тип числа
        if not isinstance(value, (int, float)):
            raise ValueError('некорректные координаты и параметры прямоугольника')

        # Проверка на положительность ширины и высоты
        if key in ('_width', '_height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError("аргументом метода is_collision() должен быть объект класса Rect")

        # Условие пересечения
        if not (self._x + self._width <= rect._x or
                rect._x + rect._width <= self._x or
                self._y + self._height <= rect._y or
                rect._y + rect._height <= self._y):
            raise TypeError('прямоугольники пересекаются')


# Функция-помощник для проверки без остановки программы
def check_collision(r1, r2):
    try:
        r1.is_collision(r2)
        return False  # Исключения нет -> не пересекаются
    except TypeError:
        return True  # Исключение есть -> пересекаются


# Создаем список объектов
lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1)
]

# Формируем список непересекающихся объектов
lst_not_collision = [
    r for r in lst_rect
    if not any(check_collision(r, other) for other in lst_rect if r is not other)
]