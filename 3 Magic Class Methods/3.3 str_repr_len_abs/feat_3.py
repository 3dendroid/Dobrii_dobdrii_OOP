class Model:
    def __init__(self):
        self.fields = {}

    def query(self, **kwargs):
        self.fields.update(kwargs)

    def __str__(self):
        if self.fields:
            return "Model: " + ", ".join(f"{key}={value}" for key, value in self.fields.items())
        return "Model"


# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)
