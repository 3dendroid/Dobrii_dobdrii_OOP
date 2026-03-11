class Phone:
    def __init__(self, model):
        self.__model = model


class SmartPhone(Phone):
    def __init__(self, model, memory):
        super().__init__(model)
        self.__memory = memory

    def get_info(self):
        return self.__model, self.__memory
