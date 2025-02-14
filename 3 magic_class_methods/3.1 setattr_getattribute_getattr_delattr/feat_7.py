class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "Вконтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "Вконтакте"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phones):
        self.name = "Phone"
        self.phone_list = phones
