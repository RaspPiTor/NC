import itertools
import random

import board_manager

def semi_AI3(board, player=0, enemy=1):
    size = board.size
    for i in range(size ** 2):
        b = board.copy()
        if b.set(i // size, i % size, player):
            if b.winner() == player:
                return i // size, i % size
    for i in range(size ** 2):
        b = board.copy()
        if b.set(i // size, i % size, enemy):
            if b.winner() == enemy:
                return i // size, i % size
    if size % 2 == 1:
        middle = [(size ** 2 + 1)//2 - 1]
    else:
        middle = [(size ** 2 - size)//2, (size ** 2 - size)//2 - 1]
        middle.extend([middle[0] + size, middle[1] + size])
    corners = [0, size - 1, size * (size - 1),
               size ** 2 - 1]
    for i in middle + corners + list(range(size ** 2)):
        b = board.copy()
        if b.set(i // size, i % size, player):
            return i // size, i % size








