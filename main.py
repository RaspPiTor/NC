from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import random

import board_manager
import AI
class ButtonHandler():
    def __init__(self, function, *parameters):
        self.function = function
        self.parameters = parameters
    def get(self):
        self.function(*self.parameters)

class GUIBoard(ttk.Frame):
    def __init__(self, master=None, size=8):
        ttk.Frame.__init__(self)
        self.board = board_manager.Board(size)
        self.graphic_board = []
        ttk.Label(text='Player: X').grid(row=0, column=0, sticky='w')
        if random.randint(0, 1):
            self.board.set(*AI.semi_AI3(self.board, 'O', 'X'), 'O')
        for row in range(size):
            new_row = []
            for column in range(size):
                command = ButtonHandler(self.button_pressed, row, column).get
                new_row.append(ttk.Button(self, command=command))
                new_row[-1].grid(row=row+1, column=column)
            self.graphic_board.append(new_row)
        self.after(10, self.refresh_everything)
    def button_pressed(self, row, column):
        if self.board.set(row, column, 'X'):
            winner = self.board.winner()
            self.refresh_everything()
            if not self.board.full():
                self.board.set(*AI.semi_AI3(self.board, 'O', 'X'), 'O')
    def refresh_everything(self):
        for row in range(self.board.size):
            for column in range(self.board.size):
                self.graphic_board[row][column]['text'] = self.board.get(row, column)
        if self.board.winner() or self.board.full():
            messagebox.Message(message='Winner is %s' % self.board.winner()).show()
            self.board = board_manager.Board(self.board.size)
        self.after(10, self.refresh_everything)
gui = GUIBoard()
gui.grid()
gui.mainloop()
