from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import random
import queue

import board_manager
import AI

import threading
class ThreadedBoardHandler(threading.Thread):
    def __init__(self, q_pmoves, q_display, board):
        self.q_pmoves = q_pmoves
        self.q_display = q_display
        self.board = board
    def run(self):
        while True:
            pass


class ButtonHandler():
    def __init__(self, function, *parameters):
        self.function = function
        self.parameters = parameters
    def get(self):
        self.function(*self.parameters)

class GUIBoard(ttk.Frame):
    def __init__(self, master=None, size=30):
        ttk.Frame.__init__(self)
        self.board = board_manager.Board(size)
        self.graphic_board = []
        ttk.Label(self, text='Player: X').grid(row=0, column=0, columnspan=4)
        ttk.Button(self, text='Reset',
                   command=self.reset).grid(row=0,column=1, columnspan=8)
        self.AI = AI.semi_AI3(size)
        self.queue = queue.Queue()
        for row in range(size):
            new_row = []
            for column in range(size):
                command = ButtonHandler(self.button_pressed, row, column).get
                new_row.append(ttk.Button(self, command=command, width=2))
                new_row[-1].grid(row=row+1, column=column)
            self.graphic_board.append(new_row)
        if random.randint(0, 1):
            ai_row, ai_column = self.AI.get(self.board, 'O', 'X')
            self.board.set(ai_row, ai_column, 'O')
            self.graphic_board[ai_row][ai_column]['text'] = 'O'
        self.after(10, self.refresh_everything)
    def button_pressed(self, row, column):
        self.queue.put((row, column))
        print(row, column)
    def refresh_everything(self):
        if self.board.winner() or self.board.full():
            messagebox.Message(message='Winner is %s' % self.board.winner()).show()
            self.reset()
        else:
            try:
                row, column = self.queue.get(0)
                if self.board.set(row, column, 'X'):
                    self.graphic_board[row][column]['text'] = 'X'
                    self.update()
                    if not self.board.full():
                        ai_row, ai_column = self.AI.get(self.board, 'O', 'X')
                        self.board.set(ai_row, ai_column, 'O')
                        self.graphic_board[ai_row][ai_column]['text'] = 'O'
            except queue.Empty:
                pass
        self.after(10, self.refresh_everything)
    def reset(self):
        self.board = board_manager.Board(self.board.size)
        self.AI = AI.semi_AI3(self.board.size)
        for row in range(self.board.size):
            for column in range(self.board.size):
                self.graphic_board[row][column]['text'] = ' '
        self.queue = queue.Queue()
gui = GUIBoard()
gui.grid()
gui.mainloop()
