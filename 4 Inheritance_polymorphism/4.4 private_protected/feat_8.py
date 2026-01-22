class Aircraft:
    def __init__(self, model, mass, speed, top):
        if not isinstance(model, str) or \
           not isinstance(mass, (int, float)) or mass <= 0 or \
           not isinstance(speed, (int, float)) or speed <= 0 or \
           not isinstance(top, (int, float)) or top <= 0:
            raise TypeError('неверный тип аргумента')

        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        if not isinstance(chairs, int) or chairs <= 0:
            raise TypeError('неверный тип аргумента')

        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')

        super().__init__(model, mass, speed, top)
        self._weapons = weapons


planes = [
    PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
    PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
    WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]
