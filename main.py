import tkinter as tk
from tkinter import messagebox

game_win = tk.Tk()
game_win.title("The Game 'Krestiki'")
game_win.geometry("300x400")
game_win.resizable(False, False)

buttons = []
button_text = "X"


def win_creation():

    for i in range(3):
        row_buttons = []
        for j in range(3):
            but = tk.Button(game_win, text="", width=5, height=2, font = ("Arial", 10),
                                    command=lambda row_w=i, col_w=j: button_click(row_w, col_w))
            row_buttons.append(but)
            but.grid(row = i, column = j)
        buttons.append(row_buttons)

    new_game_but = tk.Button(game_win, text = "New Game", width=5, height=2, font = ("Arial", 10),
                             command = lambda: new_game())
    new_game_but.grid(row = 5, column = 2)


def new_game():
    pass


def button_click(row, col):
    pass

win_creation()


game_win.mainloop()