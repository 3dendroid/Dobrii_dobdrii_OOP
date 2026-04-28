class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(str(x) for x in self)

    def __repr__(self):
        return ' '.join(str(x) for x in self)


digits = list(map(float, input().split()))

try:
    tl = TupleLimit(digits, 5)
    print(tl)
except ValueError as e:
    print(e)