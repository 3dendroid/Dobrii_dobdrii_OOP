class Point:
    MIN_COORD = 10
    MAX_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("Access denied!")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError("Access denied!")
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value

    def __getattr__(self, item):
        return False
        # print("__getattr__ " + item)

    def __delattr__(self, item):
        print("__delattr__ " + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.y
print(pt1.__dict__)
