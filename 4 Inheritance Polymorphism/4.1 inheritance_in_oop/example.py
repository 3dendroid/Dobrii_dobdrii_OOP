class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Primitive draw')


class Line(Geom):
    name = 'Line'
    def draw(self):
        print('Line draw')


class Rect(Geom):
    def draw(self):
        print('Rectangle draw')
    # pass


l = Line()
r = Rect()
l.draw()
r.draw()
print(l.name)
print(r.name)
