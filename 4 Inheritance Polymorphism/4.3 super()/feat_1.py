class Phone:
    def get_info(self):
        return "Phone"


class SmartPhone(Phone):
    def call(self):
        pass

    def get_info(self):
        return "SmartPhone"

p = Phone()
sp = SmartPhone()
print(p.get_info())
print(sp.get_info())