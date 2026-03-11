import sys

# Разбираем входные строки
lst_in = list(map(str.strip, sys.stdin.readlines()))

class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        # Хеш по комбинации name и author без учёта регистра
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        if not isinstance(other, BookStudy):
            return NotImplemented
        return (self.name.lower(), self.author.lower()) == (other.name.lower(), other.author.lower())

# Создаем список объектов из входных строк
lst_bs = []
for line in lst_in:
    # каждая строка: "Название; автор; год"
    parts = [part.strip() for part in line.split(';')]
    name, author, year_str = parts
    year = int(year_str)
    bs = BookStudy(name, author, year)
    lst_bs.append(bs)

# Подсчитываем количество уникальных объектов по хешу
unique_books = len(set(lst_bs))

# Теперь в переменной unique_books хранится нужное целое число
