class LimitException(Exception):
    """Превышение лимита"""


error = LimitException('превышение лимита нагрузки')
raise error
