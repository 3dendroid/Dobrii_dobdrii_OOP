class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self._segments = []

    def add_point(self, x, y, speed):
        self._segments.append((x, y, speed))

    def __getitem__(self, ind):
        if not isinstance(ind, int) or not (0 <= ind < len(self._segments)):
            raise IndexError('некорректный индекс')
        x, y, speed = self._segments[ind]
        return (x, y), speed

    def __setitem__(self, ind, new_speed):
        if not isinstance(ind, int) or not (0 <= ind < len(self._segments)):
            raise IndexError('некорректный индекс')
        x, y, _old = self._segments[ind]
        self._segments[ind] = (x, y, new_speed)
