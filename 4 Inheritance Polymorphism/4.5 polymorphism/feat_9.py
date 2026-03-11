class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []

        if len(args) == 2 and all(isinstance(a, (int, float)) for a in args):
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            for pt in args:
                self.__points.append(pt)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        if self.__points:
            self.__points.pop()

    def pop_front(self):
        if self.__points:
            self.__points.pop(0)
