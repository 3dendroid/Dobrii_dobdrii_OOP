class SoftList(list):
    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return False
