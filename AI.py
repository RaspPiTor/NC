import itertools
import random

import board_manager

class semi_AI3():
    def __init__(self, size=3):
        if size % 2 == 1:
            middle = [(size ** 2 + 1)//2 - 1]
        else:
            middle = [(size ** 2 - size)//2, (size ** 2 - size)//2 - 1]
            middle.extend([middle[0] + size, middle[1] + size])
        corners = [0, size - 1, size * (size - 1), size ** 2 - 1]
        edges = list(range(size)) + list(range(size**2 - size, size ** 2))
        edges += list(range(0, size ** 2, size))
        edges += list(range(size - 1, size ** 2 - size, size))
        diagonals = [size * i + i for i in range(size)]
        diagonals += [size * i + size - i - 1for i in range(size)]
        self.to_do = middle + corners + edges + diagonals
        self.to_do.extend(i for i in range(size ** 2) if i not in self.to_do)
        self.size = size
    def get(self, board, player, enemy):
        size = self.size
        to_do = self.to_do
        for i in to_do:
            b = board.copy()
            if b.quick_set(i, player):
                if b.winner() == player:
                    to_do.remove(i)
                    return i // size, i % size
        for i in to_do:
            b = board.copy()
            if b.quick_set(i, enemy):
                if b.winner() == enemy:
                    to_do.remove(i)
                    return i // size, i % size
        for i in to_do:
            b = board.copy()
            if b.can_set(i):
                to_do.remove(i)
                return i // size, i % size
