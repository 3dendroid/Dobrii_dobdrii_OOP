# class Point3D:
#     def __init__(self, x, y, z):
#         self._x = x
#         self._y = y
#         self._z = z
#
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise ValueError('Type error')
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, coord):
#         self.verify_coord(coord)
#         self._x = coord
#
#     @property
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, coord):
#         self.verify_coord(coord)
#         self._y = coord
#
#     @property
#     def z(self):
#         return self._z
#
#     @z.setter
#     def z(self, coord):
#         self.verify_coord(coord)
#         self._z = coord
#
#
# p = Point3D(1, 2, 3)
# print(p.__dict__)


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise ValueError('Type error')

    def __set__name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


p = Point3D(1, 2, 3)
p.__dict__['xr'] = 7
# p.xr = 5
print(p.xr,p.__dict__)
