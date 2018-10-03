class Board():
    def __init__(self, size=3, board=None):
        self.board = board if board else [' ' for i in range(size ** 2)]
        self.size = size
    def set(self, row, column, player):
        if self.board[row * self.size + column] == ' ':
            self.board[row * self.size + column] = player
            return True
    def quick_set(self, i, player):
        if self.board[i] == ' ':
            self.board[i] = player
            return True
    def can_set(self, i):
        return self.board[i] == ' '
    def get(self, row, column):
        return self.board[row * self.size + column]
    def winner(self):
        size = self.size
        board = self.board
        for row in range(0, size ** 2, size):
            if board[row] != ' ':
                if all(i == board[row] for i in board[row:row+size]):
                    return board[row]
        for c in range(size):
            if board[c] != ' ':
                if all(board[c] == board[size * row + c] for row in range(size)):
                    return board[c]
        if board[0] != ' ':
            if all(board[0] == board[size * i + i] for i in range(size)):
                return board[0]
        if board[size - 1] != ' ':
            if all(board[size - 1] == board[size * i - i + size - 1] for i in range(size)):
                return board[size - 1]
        return None
    def full(self):
        return not ' ' in self.board
    def copy(self):
        return Board(self.size, self.board.copy())
