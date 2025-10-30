class SmartPhone:


    pass


class IPhone(SmartPhone):


    pass

phone = IPhone()

# print('isinstance(phone, SmartPhone): ', isinstance(phone, SmartPhone))
# print('issubclass(IPhone, SmartPhone): ', issubclass(IPhone, SmartPhone))
# print('issubclass(SmartPhone, IPhone): ', issubclass(SmartPhone, IPhone))
# print('issubclass(SmartPhone, IPhone): ', issubclass(SmartPhone, IPhone))
# print('issubclass(IPhone, object): ', issubclass(IPhone, object))

try:
    print(issubclass(IPhone, object))
except TypeError:
    print("issubclass(phone, SmartPhone): Ошибка TypeError при вызове")
