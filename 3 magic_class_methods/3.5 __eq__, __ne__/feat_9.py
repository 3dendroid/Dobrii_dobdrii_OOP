class Body:
    def __init__(self, name: str, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def mass(self) -> float:
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.mass() == other.mass()
        elif isinstance(other, (int, float)):
            return self.mass() == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.mass() < other.mass()
        elif isinstance(other, (int, float)):
            return self.mass() < other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Body):
            return self.mass() > other.mass()
        elif isinstance(other, (int, float)):
            return self.mass() > other
        return NotImplemented
