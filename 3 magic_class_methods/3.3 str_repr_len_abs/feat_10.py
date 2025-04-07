class PolyLine:
    def __init__(self, *coords):
        self._coords = list(coords)

    def add_coord(self, x, y):
        self._coords.append((x, y))

    def remove_coord(self, indx):
        del self._coords[indx]

    def get_coords(self):
        return self._coords
