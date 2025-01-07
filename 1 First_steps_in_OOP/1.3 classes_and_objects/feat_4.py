class Goods:
    title: str = "Мороженое"
    weight: int = 154
    tp: str = "Еда"
    price: int = 1024


Goods.price = 2048
Goods.inflation = 100

print(Goods.__dict__)
