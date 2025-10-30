# class Geom:
#     pass
#
#
# class Line(Geom):
#     pass
#
#
# g = Geom()
# l = Line()
# print(l.__class__)


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
