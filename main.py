from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import random
import queue

import board_manager
import AI

import threading
class ThreadedMatchManager(threading.Thread):
    def __init__(self, q_pmoves, q_display, size=3):
        threading.Thread.__init__(self)
        self.q_pmoves = q_pmoves
        self.q_display = q_display
        self.size = size
    def run(self):
        q_pmoves = self.q_pmoves
        q_display = self.q_display
        command = ['reset']
        while True:
            if command[0] == 'reset':
                board = board_manager.Board(size=self.size)
                ai = AI.semi_AI3(self.size)
                if random.randint(0, 1):
                    ai_row, ai_column = ai.get(board, 'O', 'X')
                    board.set(ai_row, ai_column, 'O')
                    q_display.put(('put', ai_row, ai_column, 'O'))
            elif command[0] == 'put':
                row, column = command[1:]
                if board.set(row, column, 'X'):
                    q_display.put(('put', row, column, 'X'))
                    if not board.full():
                        ai_row, ai_column = ai.get(board, 'O', 'X')
                        board.set(ai_row, ai_column, 'O')
                        q_display.put(('put', ai_row, ai_column, 'O'))
            else:
                print('Unknown command', command)
            if board.winner() or board.full():
                q_display.put(('end_game', board.winner()))
            command = q_pmoves.get()


class ButtonHandler():
    def __init__(self, function, *parameters):
        self.function = function
        self.parameters = parameters
    def get(self):
        self.function(*self.parameters)

class GUIBoard(ttk.Frame):
    def __init__(self, master=None, size=30):
        ttk.Frame.__init__(self)
        self.size = size
        self.graphic_board = []
        ttk.Label(self, text='Player: X').grid(row=0, column=0, columnspan=4)
        ttk.Button(self, text='Reset',
                   command=self.reset).grid(row=0,column=4, columnspan=8)
        
        self.q_pmoves = queue.Queue()
        self.q_display = queue.Queue()
        self.threaded_match_manager = ThreadedMatchManager(self.q_pmoves,
                                                           self.q_display,
                                                           size)
        self.threaded_match_manager.start()
        for row in range(size):
            new_row = []
            for column in range(size):
                command = ButtonHandler(self.button_pressed, row, column).get
                new_row.append(ttk.Button(self, command=command, width=2))
                new_row[-1].grid(row=row+1, column=column)
            self.graphic_board.append(new_row)
        self.after(10, self.refresh_everything)
    def button_pressed(self, row, column):
        self.q_pmoves.put(('put', row, column))
    def refresh_everything(self):
        try:
            while True:
                command = self.q_display.get(0)
                if command[0] == 'put':
                    row, column, player= command[1:]
                    self.graphic_board[row][column]['text'] = player
                elif command[0] == 'end_game':
                    messagebox.Message(message='Winner is %s' % command[1]).show()
                    self.reset()
        except queue.Empty:
            pass
        self.after(100, self.refresh_everything)
    def reset(self):
        self.q_pmoves.put(('reset', ))
        for row in range(self.size):
            for column in range(self.size):
                self.graphic_board[row][column]['text'] = ' '
gui = GUIBoard()
gui.grid()
gui.mainloop()
