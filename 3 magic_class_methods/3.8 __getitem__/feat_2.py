class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_attrs__ = len(kwargs)
        self.__attrs__ = tuple(self.__dict__.keys())

    def __check_index(self, index):
        if type(index) != int or not (-self.__total_attrs__ < index < self.__total_attrs__):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.__attrs__[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.__attrs__[key], value)
