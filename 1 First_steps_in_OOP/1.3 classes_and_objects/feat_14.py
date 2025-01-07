class Magazine:
    name: str = 'Наука и жизнь'
    price: int = 1101


print(getattr(Magazine, 'id'))
