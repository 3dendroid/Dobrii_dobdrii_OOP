import math


# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("!@#$%^&*() -_=+[]{};:,.<>/?")
# s2 = StripChars(" ")
# res = s1(" Hello World! @%!")
# res2 = s2("     H ell oW or ld! ")
# print(res, res2, sep="\n")


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def df_sin(x):
    return math.sin(x)

# df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))
