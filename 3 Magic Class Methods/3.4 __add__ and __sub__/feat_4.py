class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("Right operand must be list or NewList")
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Right operand must be list or NewList")
        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res
