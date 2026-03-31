from dataclasses import dataclass


@dataclass(init=False, repr=False)
class Volume:
    height: int
    width: int
    depth: int

    def get_volume(self):
        return self.height * self.width * self.depth


v = Volume()
v.height = 10
v.width = 20
v.depth = 30

res = v.get_volume()