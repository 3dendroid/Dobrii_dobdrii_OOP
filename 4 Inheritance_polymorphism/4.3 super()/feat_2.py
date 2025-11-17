class SmartPhone:
    def call(self):
        pass

    def get_info(self):
        return "SmartPhone"


class IPhone(SmartPhone):
    def __init__(self, model):
        self.model = model

    def get_info(self):
        return super().get_info() + ": IPhone " + self.model


s = SmartPhone()
print(s.get_info())
