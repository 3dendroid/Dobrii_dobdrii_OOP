# программу не менять, только добавить два метода
# lst_in = list (map (str.strip, sys.stdin.readlines ()))  # считывание списка строк из входного потока

lst_in = ['1 Сергей 35 12000', '2 Федор 25 124500', '3 Иван 27 213000']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
