import itertools
import random

import board_manager
def AIvsAI(ai1, ai2, runs=1):
    ai = [ai1, ai2]
    ai_score = [0, 0]
    for i in range(runs):
        for player in (0,1):
            board = board_manager.Board()
            while not board.full() and not board.winner():
                row, column = ai[player](board.board.copy(), player)
                if not board.set(row, column, player):
                    print(player, 'did invalid move')
                player = int(not player)
            winner = board.winner()
            if winner is not None:
                ai_score[winner] += .5
            else:
                ai_score[0] += .25
                ai_score[1] += .25
                print('Draw between %s and %s' % (ai1.__name__, ai2.__name__))
    return ai_score[0], ai_score[1]

def first_empty(board, player=0):
    location = board.index(' ')
    return location // 3, location % 3
def random_AI(board, player=0):
    location = random.choice([i for i, x in enumerate(board) if x == ' '])
    return location // 3, location % 3
def semi_AI1(board, player=0):
    for i in [4] + [0,2,6,8] + [1,3,5,7]:
        if board[i] == ' ':
            return i // 3, i % 3
def semi_AI2(board, player=0):
    for i in [4] + [1,3,5,7] + [0,2,6,8]:
        if board[i] == ' ':
            return i // 3, i % 3
def semi_AI3(board, player=0, enemy=1):
    for i in range(9):
        b = board.copy()
        if b.set(i // 3, i % 3, player):
            if b.winner() == player:
                return i // 3, i % 3
    for i in range(9):
        b = board.copy()
        if b.set(i // 3, i % 3, enemy):
            if b.winner() == enemy:
                return i // 3, i % 3
    for i in [4] + [1,3,5,7] + [0,2,6,8]:
        b = board.copy()
        if b.set(i // 3, i % 3, player):
            return i // 3, i % 3


##potential = [first_empty, random_AI, semi_AI1, semi_AI2, semi_AI3]
##potential = [[i, 0] for i in potential]
##for pot1, pot2 in itertools.combinations(potential, 2):
##    pot1_score, pot2_score = AIvsAI(pot1[0], pot2[0], 1)
##    print(pot1[0].__name__,pot1_score,  pot2[0].__name__, pot2_score)
##    pot1[1] += pot1_score
##    pot2[1] += pot2_score
##function, score = max(potential, key=lambda x: x[1])
##print(function.__name__, score)









