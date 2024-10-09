class Car:
    pass


# Car.__setattr__ (Car, 'model', 'Тойота')
# Car.__setattr__ (Car, 'color', 'Розовый')
# Car.__setattr__ (Car, 'number', 'П111УУ77')

Car.model = 'Тойота'
Car.color = 'Розовый'
Car.number = 'П111УУ77'

# print (Car.__dict__['color'])
print (Car.color)
