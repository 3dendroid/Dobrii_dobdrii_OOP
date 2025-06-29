class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if None not in (x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def __bool__(self):
        return all(hasattr(self, attr) for attr in ("x1", "y1", "x2", "y2"))

    def get_coords(self):
        # Проверяем наличие перед возвратом
        if not self:
            raise AttributeError("нет координат для извлечения")
        return (self.x1, self.y1, self.x2, self.y2)

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]