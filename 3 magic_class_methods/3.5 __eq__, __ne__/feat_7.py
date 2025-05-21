# объявление класса
class FileAcceptor:
    def __init__(self, *exts):
        # сохраняем уникальные расширения в нижнем регистре
        self._exts = set(ext.lower() for ext in exts)

    def __call__(self, filename):
        # пытаемся выделить часть после последней точки
        parts = filename.lower().rsplit('.', 1)
        if len(parts) == 2:
            return parts[1] in self._exts
        return False

    def __add__(self, other):
        # объединяем множества расширений и возвращаем новый FileAcceptor
        return FileAcceptor(*(self._exts | other._exts))


# пример использования (эти строки в программе писать не нужно)
if __name__ == "__main__":
    filenames = [
        "boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
        "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"
    ]
    acceptor_images = FileAcceptor("jpg", "jpeg", "png")
    acceptor_docs = FileAcceptor("txt", "doc", "xls")

    # отфильтруем только изображения и документы
    result = list(filter(acceptor_images + acceptor_docs, filenames))
    print(result)
    # ['boat.jpg', 'ans.web.png', 'text.txt', 'www.python.doc',
    #  'my.ava.jpg', 'forest.jpeg', 'eq_1.png', 'eq_2.xls']
