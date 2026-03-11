from collections import Counter

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if not isinstance(other, Thing):
            return NotImplemented
        return (self.name.lower(), self.mass) == (other.name.lower(), other.mass)

    def __ne__(self, other):
        eq = self.__eq__(other)
        return NotImplemented if eq is NotImplemented else not eq

class Box:
    def __init__(self):
        self._things = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self._things.append(obj)
        else:
            raise TypeError("Only Thing instances can be added")

    def get_things(self):
        return list(self._things)

    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        # Считаем, сколько каждого предмета по (name.lower(), mass)
        def key(t: Thing):
            return (t.name.lower(), t.mass)
        cnt1 = Counter(key(t) for t in self._things)
        cnt2 = Counter(key(t) for t in other._things)
        return cnt1 == cnt2

    def __ne__(self, other):
        eq = self.__eq__(other)
        return NotImplemented if eq is NotImplemented else not eq
