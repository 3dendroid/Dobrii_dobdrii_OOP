class Interface:
    def set_data(self, data):
        pass

    def update(self):
        raise NotImplementedError

    def abstract(self):
        return self