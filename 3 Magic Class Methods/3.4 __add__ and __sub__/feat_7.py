class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            del self.book_list[other]
        elif isinstance(other, Book):
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.book_list)
