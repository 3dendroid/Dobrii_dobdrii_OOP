class Person:
    name: str = 'Сергей Балакирев'
    job: str = 'Программист'
    city: str = 'Москва'


p1 = Person()

if hasattr(p1, 'job') in p1.__dict__:
    print(True)
else:
    print(False)
