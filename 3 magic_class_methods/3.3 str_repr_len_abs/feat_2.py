import sys


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'


lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(lst_in[0], lst_in[1], int(lst_in[2]))
print(book)
