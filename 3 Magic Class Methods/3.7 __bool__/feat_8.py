import random


class Cell:
    def __init__(self):
        # приватные атрибуты
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, val):
        if not isinstance(val, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = val

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        if not isinstance(val, int) or not (0 <= val <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = val

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        if not isinstance(val, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = val

    def __bool__(self):
        # возвращаем True, если клетка закрыта, иначе False
        return not self.__is_open


class GamePole:
    _instance = None

    def __new__(cls, n, m, total_mines):
        # singleton: если экземпляр уже создан, возвращаем его
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, n, m, total_mines):
        # параметры поля
        self._n = n
        self._m = m
        self._total_mines = total_mines
        # создаём непересекающийся кортеж списков Cell
        # изначально все клетки без мин, с number=0, is_open=False
        cells = [[Cell() for _ in range(m)] for _ in range(n)]
        self.__pole_cells = tuple(tuple(row) for row in cells)

    @property
    def pole(self):
        # только для чтения
        return self.__pole_cells

    def init_pole(self):
        n, m, t = self._n, self._m, self._total_mines
        # сброс старых значений
        for i in range(n):
            for j in range(m):
                cell = self.__pole_cells[i][j]
                cell.is_mine = False
                cell.number = 0
                cell.is_open = False

        # расставляем t мин случайно
        all_coords = [(i, j) for i in range(n) for j in range(m)]
        mines = random.sample(all_coords, t)
        for i, j in mines:
            self.__pole_cells[i][j].is_mine = True

        # вычисляем числа вокруг мин
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(n):
            for j in range(m):
                cell = self.__pole_cells[i][j]
                if cell.is_mine:
                    continue
                cnt = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if self.__pole_cells[ni][nj].is_mine:
                            cnt += 1
                cell.number = cnt

    def open_cell(self, i, j):
        # проверка корректности индексов
        if not (0 <= i < self._n and 0 <= j < self._m):
            raise IndexError("некорректные индексы i, j клетки игрового поля")
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        # простая текстовая отрисовка:
        # • — закрытая клетка, * — мина, число — открытая
        for row in self.__pole_cells:
            line = []
            for cell in row:
                if not cell.is_open:
                    line.append('•')
                elif cell.is_mine:
                    line.append('*')
                else:
                    line.append(str(cell.number))
            print(' '.join(line))
