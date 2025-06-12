class User:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def __len__(self):
        return self.old

user1 = User('Sergey', 45)
user2 = User('Петр', 0)

print(bool(user1))
print(bool(user2))