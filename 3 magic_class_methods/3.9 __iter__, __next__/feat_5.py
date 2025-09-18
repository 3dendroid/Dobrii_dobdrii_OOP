class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._len_attrs = len(self._attrs)
        self._iter_index = -1

    def __check_index(self, index):
        if type(index) != int or not (-self._len_attrs <= index < self._len_attrs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self._attrs[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self._attrs[key], value)

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < self._len_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        raise StopIteration
