class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2


v = Vector(10, 20)
print(Vector.norm2(5, 6))

language = 'Я глобальный'


class DepartmentIT:
    language = 'Я в Классе'

    def __init__(self, name):
        self.language = name

    def get_info1(типо_self):
        print('get_info1', типо_self.language)

    def get_info2(self):
        print('get_info2', self.language)

    @classmethod
    def get_info3(cls):
        print('get_info3', cls.language)

    @classmethod
    def get_info4(cls):
        print('get_info4', DepartmentIT.language)

    @classmethod
    def get_info5(cls):
        print('get_info5', language)

    def get_info6(self):
        print('get_info6', language)

    @staticmethod
    def get_info7():
        print('get_info7', language)

    @staticmethod
    def get_info8():
        print('get_info7', DepartmentIT.language)


x = DepartmentIT('Я в экземпляре')
x.get_info1()  # get_info1 Я в экземпляре
x.get_info2()  # get_info2 Я в экземпляре
x.get_info3()  # get_info3 Я в Классе
x.get_info4()  # get_info4 Я в Классе
x.get_info5()  # get_info5 Я глобальный
x.get_info6()  # get_info6 Я глобальный
x.get_info7()  # get_info7 Я глобальный
x.get_info8()  # get_info8 Я в Классе
