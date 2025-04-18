class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.lst = list(args)

    def add_ingredient(self, ing):
        self.lst.append(ing)

    def remove_ingredient(self, ing):
        self.lst.remove(ing)

    def get_ingredients(self):
        return tuple(self.lst)

    def __len__(self):
        return len(self.lst)
