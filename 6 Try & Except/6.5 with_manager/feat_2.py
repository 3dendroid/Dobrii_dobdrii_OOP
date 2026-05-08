# здесь объявляйте класс PrimaryKey
class PrimaryKey:
    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return r'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


with PrimaryKey() as pk:
    raise ValueError