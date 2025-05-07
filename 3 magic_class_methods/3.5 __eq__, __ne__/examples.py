# __eq__ → equal (равно, ==)
# __ne__ → not equal (не равно, !=)
# __lt__ → less than (меньше, <)
# __le__ → less than or equal to (меньше или равно, <=)
# __gt__ → greater than (больше, >)
# __ge__ → greater than or equal to (больше или равно, >=)

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('seconds must be int')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('right operant must be int or Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(2000)

print(c1 > c2)
