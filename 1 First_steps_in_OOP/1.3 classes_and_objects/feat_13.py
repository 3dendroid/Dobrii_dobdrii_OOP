class Point:
    tp: str = 'Точка'


# delattr (Point, "tp")
# del Point.tp

print(Point.__dict__)
