from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """Абстрактный метод для получения первичного ключа"""
        pass

    def get_info(self):
        """Обычный метод базового класса"""
        return "Базовый класс Model"


class ModelForm(Model):
    _count = 0  # Статический счетчик для генерации уникальных _id

    def __init__(self, login, password):
        # Увеличиваем счетчик и присваиваем уникальный id
        ModelForm._count += 1
        self._id = ModelForm._count

        # Сохраняем логин и пароль в локальных атрибутах
        self._login = login
        self._password = password

    def get_pk(self):
        """Переопределенный метод, возвращающий уникальный _id объекта"""
        return self._id