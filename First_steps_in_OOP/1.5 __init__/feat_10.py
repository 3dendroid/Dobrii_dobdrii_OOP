from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell () for n in range (self._n)] for n in range (self._n)]
        self.init ()

    def init(self):
        m = 0
        while m < self._m:
            i = randint (0, self._n - 1)
            j = randint (0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range (self._n):
            for y in range (self._n):
                if not self.pole[x][y].mine:
                    mines = sum (
                        self.pole[x + i][y + j].mine for i, j in indx if 0 <= x + i < self._n and 0 <= y + j < self._n)
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print (*map (lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole (10, 12)

# import random
#
#
# def count_mines_around(pole, I, J):
#     '''Функция для расчета количества соседних мин'''
#     mines = 0
#     for i in range (I - 1, I + 2):
#         for j in range (J - 1, J + 2):
#             if pole[i][j].mine and (I != i or J != j):
#                 mines += 1
#     return mines
#
#
# def constr_pole(N, M):
#     '''Функция для конструирования поля, возвращает вложенный список N*N
#     с ячейками класса Cell, из которых M случайных - заминированы'''
#
#     pole = [[0 for i in range (N + 2)] for j in range (N + 2)]
#     # Для рассчета крайних точек, обрамляем поле заведомо незаминированными клетками
#
#     mines = random.sample ([(i, j) for i in range (N) for j in range (N)], M)
#     # Список кортежей с координатами мин
#
#     for i in range (N + 2):
#         for j in range (N + 2):
#             m = (i - 1, j - 1)  # Смещение, чтобы не поместить мины в крайние клетки
#             pole[i][j] = Cell (mine=(m in mines))
#
#     # Обсчитываем клетки на количество соседних мин
#     for i in range (1, N + 1):
#         for j in range (1, N + 1):
#             pole[i][j].around_mines = count_mines_around (pole, i, j)
#
#     # Обрезаем рамку
#     res = [[0 for i in range (N)] for j in range (N)]
#     for i in range (1, N + 1):
#         for j in range (1, N + 1):
#             res[i - 1][j - 1] = pole[i][j]
#     return res
#
#
# class Cell:
#     '''Класс ячеек'''
#
#     def __init__(self, mine, around_mines=0):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     '''Класс игрового поля'''
#
#     def __init__(self, N, M):
#         assert N ** 2 >= M, 'Мин больше, чем клеток'
#         self.N = N
#         self.M = M
#         self.pole = constr_pole (self.N, self.M)
#
#     def init(self):
#         '''Обновить поле'''
#         self.pole = constr_pole (self.N, self.M)
#
#     def show(self):
#         '''Показать поле'''
#         for i in range (self.N):
#             for j in range (self.N):
#                 if not self.pole[i][j].fl_open:
#                     print ('#', end=' ')
#                 elif self.pole[i][j].mine:
#                     print ('*', end=' ')
#                 else:
#                     print (self.pole[i][j].around_mines, end=' ')
#             print ()
#
#
# pole_game = GamePole (10, 12)