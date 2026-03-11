class Book:  # name of class
    title: 'title'  # attribute of class
    pages: 143

    def set_title(self, title):  # method of class
        pass


book_1 = Book()  # object of class (examples of classes)
book_2 = Book()

book_1.year = 2024  # local attributes of class
book_1.name = 'Book of Jungle'
book_2.title = 'Notebook'
book_2.pages = 251

print(book_2.title)
print(book_1.year)
