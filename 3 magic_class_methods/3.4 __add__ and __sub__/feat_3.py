class Way:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        return Way(self.length + other.length)

    def __radd__(self, other):
        return Way(self.length + other.length)

    def __iadd__(self, other):
        return Way(self.length + other.length)


w1 = Way(5)
w2 = Way(10)
