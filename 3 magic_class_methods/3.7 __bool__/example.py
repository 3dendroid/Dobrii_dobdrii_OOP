class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x * self.y + self.x * self.y

    def __bool__(self):
        print('__bool__')
        return self.x == self.y


p = Point(111, 111)
if p:
    print('Obj p is True')
else:
    print('Obj p is False')
