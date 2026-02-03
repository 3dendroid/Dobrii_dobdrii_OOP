class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value):
        return self._is_valid(value)

    def _is_valid(self, data):
        if type(data) is not float:
            return False
        return self._min_value <= data <= self._max_value
