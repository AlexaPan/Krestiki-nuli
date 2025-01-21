import tkinter as tk
from tkinter import messagebox

game_win = tk.Tk()
game_win.title("The Game 'Krestiki'")
game_win.geometry("300x400")
game_win.resizable(False, False)

buttons = []
button_text = "X"


def win_creation():
    # Создаем фрейм для кнопок 3x3
    frame = tk.Frame(game_win)
    frame.pack()

    #create 3x3 buttons
    for i in range(3):
        row_buttons = []
        for j in range(3):
            but = tk.Button(frame, text="", width=5, height=2, font = ("Arial", 10), background="white",
                                    command=lambda row_w=i, col_w=j: button_click(row_w, col_w))
            row_buttons.append(but)
            but.grid(row = i, column = j)
        buttons.append(row_buttons)

    #create scoreboard
    score = score_text()
    score_board = tk.Label(game_win, text = "Scoreboard", width=30, height=2, font = ("Arial", 10))
    score_board.pack(pady = 5)

    frame_score = tk.Frame(game_win)
    frame_score.pack()


    score_x = tk.Label(frame_score, text = "X: 0", width=10, height=2, font = ("Arial", 10))
    score_x.grid(row = 0, column = 0)

    score_o = tk.Label(frame_score, text = "O: 0", width=10, height=2, font = ("Arial", 10))

    #create new game button
    new_game_but = tk.Button(game_win, text = "New Game", width=20, height=2, font = ("Arial", 10),
                             command = lambda: new_game())
    new_game_but.pack(pady = 5)


def new_game():
    pass


def button_click(row, col):
    pass

def score_text():
    pass

win_creation()


game_win.mainloop()