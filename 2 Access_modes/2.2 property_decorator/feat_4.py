class Car:
    def __init__(self):
        self.model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if type(value) == str and 2 <= len(value) <= 100:
            self.__model = value
