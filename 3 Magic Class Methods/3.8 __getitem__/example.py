class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, index):
        if 0 <= index < len(self.marks):
            return self.marks[index]
        else:
            raise IndexError("Wrong index")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Key must be non-negative integer")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Key must be non-negative integer")

        del self.marks[key]


s1 = Student("Denis", [5, 2, 4, 3, 2])
del s1[2]
print(s1.marks)
