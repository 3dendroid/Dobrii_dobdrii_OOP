import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)


# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

players = []
for line in lst_in:
    name, old_str, score_str = map(str.strip, line.split(';'))
    old = int(old_str)
    score = int(score_str)
    players.append(Player(name, old, score))

players_filtered = list(filter(bool, players))
