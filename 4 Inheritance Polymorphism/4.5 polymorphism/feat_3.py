class Lector(Mentor):
    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f"Лектор {self._fio}: предмет {self._subject}"


class Reviewer(Mentor):
    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f"Эксперт {self._fio}: предмет {self._subject}"
