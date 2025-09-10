class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.table = {}

    def update_index(self):
        if not self.table:
            self.rows = self.cols = 0
            return
        self.rows = max(r for r, _ in self.table) + 1
        self.cols = max(c for _, c in self.table) + 1

    def add_data(self, rows, cols, data):
        self.table[(rows, cols)] = Cell(data)
        self.update_index()

    def remove_data(self, rows, cols):
        try:
            del self.table[(rows, cols)]
            self.update_index()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        self.table[(key[0], key[1])] = Cell(value)
        self.update_index()
