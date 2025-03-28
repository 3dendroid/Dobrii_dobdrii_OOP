class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(map(lambda x: x * x, self.__coords)) ** 0.5
