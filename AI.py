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
        self.to_do = middle + corners + list(range(size ** 2))
        self.size = size
    def get(self, board, player, enemy):
        size = self.size
        to_do = self.to_do
        for i in range(size ** 2):
            if i in to_do:
                b = board.copy()
                if b.quick_set(i, player):
                    if b.winner() == player:
                        to_do.remove(i)
                        return i // size, i % size
        for i in range(size ** 2):
            if i in to_do:
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




