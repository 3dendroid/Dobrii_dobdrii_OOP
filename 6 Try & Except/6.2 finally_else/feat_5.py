class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


pt = Point()

try:
    a, b = input().split()
    try:
        x = int(a)
        y = int(b)
        pt = Point(x, y)
    except ValueError:
        try:
            x = float(a)
            y = float(b)
            pt = Point(x, y)
        except ValueError:
            pt = Point()

except Exception as e:
    print(e)

finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")
