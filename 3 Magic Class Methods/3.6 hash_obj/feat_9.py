# Объявляем класс Dimensions
class Dimensions:
    def __init__(self, a, b, c):
        # Проверяем, что все габариты положительны
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        # Хеш вычисляем по кортежу (a, b, c)
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        if not isinstance(other, Dimensions):
            return NotImplemented
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)


# Читаем входную строку
# В формате "a1 b1 c1; a2 b2 c2; ...; aN bN cN"
input_line = input().strip()

# Разбиваем по символу ';', затем для каждой части получаем три числа
parts = [segment.strip() for segment in input_line.split(';') if segment.strip()]

# Список объектов Dimensions
lst_dims = []

for part in parts:
    # Каждая часть: "a b c"
    numbers = part.split()
    if len(numbers) != 3:
        # Неверный формат – можно выбросить ошибку, если нужно.
        raise ValueError("каждый блок должен содержать ровно три числа")
    # Конвертируем в float
    a, b, c = map(float, numbers)
    # Создаём объект (в конструкторе проверяется > 0)
    d = Dimensions(a, b, c)
    lst_dims.append(d)

# Сортируем список по возрастанию хэшей (stable-сортировка сохраняет порядок среди равных хэшей)
lst_dims.sort(key=hash)

# В этой точке lst_dims содержит объекты Dimensions,
# отсортированные по неубыванию их хэшей.
# На экран ничего выводить не нужно.
