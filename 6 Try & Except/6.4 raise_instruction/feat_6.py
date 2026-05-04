class DateError(Exception):
    """Неверный формат даты"""


class DateString:
    def __init__(self, date_string):
        try:
            parts = date_string.split('.')
            if len(parts) != 3:
                raise DateError()
            dd, mm, yyyy = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= dd <= 31 and 1 <= mm <= 12 and 1 <= yyyy <= 3000):
                raise DateError()
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
        except (ValueError, AttributeError):
            raise DateError()

    def __str__(self):
        return f"{self.dd:02d}.{self.mm:02d}.{self.yyyy:04d}"


date_string = input()

try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")
