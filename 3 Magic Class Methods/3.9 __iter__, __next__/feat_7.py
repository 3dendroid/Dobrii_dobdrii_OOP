class IterColumn:
    def __init__(self, lst, col_indx):
        self._lst = lst
        self._col_indx = col_indx

    def __iter__(self):
        for row in self._lst:
            yield row[self._col_indx]
