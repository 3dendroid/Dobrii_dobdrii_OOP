class VideoRating:
    def __init__(self):
        self.__rating = 0  # приватный атрибут

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if type(value) is not int or not (0 <= value <= 5):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()
