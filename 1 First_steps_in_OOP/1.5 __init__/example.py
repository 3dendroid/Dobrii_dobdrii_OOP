class Point:
    def __init__(self, x, y):
        print ('initialization: ' + str (self))
        self.x = x
        self.y = y

    def __del__(self):
        print ('deleting: ' + str (self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point (130, 145)
pt.set_coords (999, 666)
print (pt.get_coords ())
