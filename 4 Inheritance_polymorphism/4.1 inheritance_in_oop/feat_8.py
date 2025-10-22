class Validator:
    def _is_valid(self, data):
        # Базовый валидатор всегда принимает данные
        return True

    def __call__(self, data):
        if self._is_valid(data):
            return data
        raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        # Отвергаем bool, т.к. bool является подклассом int
        if isinstance(data, bool):
            return False
        if not isinstance(data, int):
            return False
        return self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        # Требуем именно float (int не принимаем)
        if not isinstance(data, float):
            return False
        return self.min_value <= data <= self.max_value

