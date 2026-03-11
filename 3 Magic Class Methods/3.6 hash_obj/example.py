# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(p1 == p2)
# print(hash(p1))
# print(hash(p2))

# если объекты a == b, то hash(a) == hash(b)
# если hash(a) != hash(b), то a != b

hash((5, 4, 3.5))
hash("Balakirev")
# hash([5, 4,3])
hash(1024.56)
hash(True)
# hash({1: True})