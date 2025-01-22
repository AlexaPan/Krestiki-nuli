import tkinter as tk
from math import trunc
from pickle import GLOBAL
from tkinter import messagebox

game_win = tk.Tk()
game_win.title("The Game 'Krestiki'")
game_win.geometry("400x150")
game_win.resizable(False, False)
game_win.configure(background="gray")

buttons = []
button_text = "X"
score = []


def win_creation(score):

    # create scoreboard

    frame_score = tk.Frame(game_win)
    frame_score.configure(borderwidth=1, relief="solid")
    frame_score.pack(side=tk.LEFT, pady=10)

    score_board = tk.Label(frame_score, text="Scoreboard", width=10, height=1, relief="solid", font=("Arial", 10))
    score_board.grid(row=0, column=0, padx=5, pady=5)

    score_count = tk.Label(frame_score, text="Number of games", width=15, height=1, relief="solid", font=("Arial", 10))
    score_count.grid(row=0, column=1, padx=5, pady=5)

    score_count = tk.Label(frame_score, text=f"{game_count()}", width=15, height=2, relief="solid", font=("Arial", 10))
    score_count.grid(rowspan=2, column=1, padx=5, pady=5)

    score_x = tk.Label(frame_score, text="X   0", width=10, height=1, relief="solid", font=("Arial", 10))
    score_x.grid(row=1, column=0)

    score_o = tk.Label(frame_score, text="0 - 0", width=10, height=1, relief="solid", font=("Arial", 10))
    score_o.grid(row=2, column=0)
    score.append(score_o)

    # create new game button
    new_game_but = tk.Button(frame_score, text="New Game", width=20, height=2, font=("Arial", 10),
                             command=lambda: new_game())
    new_game_but.grid(row=3, columnspan=2, pady=5)

    # Создаем фрейм для кнопок 3x3
    frame = tk.Frame(game_win)
    frame.pack(side=tk.LEFT, padx=10, pady=10)

    #create 3x3 buttons
    for i in range(3):
        row_buttons = []
        for j in range(3):
            but = tk.Button(frame, text="", width=5, height=2, font = ("Arial", 10), background="white",
                                    command=lambda row_w=i, col_w=j, score=score_o.cget("text"): button_click(row_w, col_w, score))
            row_buttons.append(but)
            but.grid(row = i, column = j)
        buttons.append(row_buttons)




def new_game():
    pass


def button_click(row, col, score):
    global button_text
    buttons[row][col]["text"] = button_text
    button_text = "O" if button_text == "X" else "X"

    if check_win():
        messagebox.showinfo("The Game 'Krestiki'", f"Победил {button_text}")
        score_text(button_text, score)
        new_game()

def check_win():
    for i in range(3)
        if (
            buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"] or
            buttons[0][i]["text"]==buttons[1][i]["text"]==buttons[2][1]["text"]
            ):
            return True
    if (
            buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] or
            buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"]
    ):
        return True

    return False


def score_text(who_win_text, score):
    current_score = score

    # Разделяем строку по символу '-'
    parts = current_score.split('-')

    # Удаляем лишние пробелы и преобразуем в целые числа
    num1 = int(parts[0].strip())
    num2 = int(parts[1].strip())

    if who_win_text == "X":
        num1 +=1
    elif who_win_text == "O":
        num2 +=1

    return f"{num1} - {num2}"

def game_count():
    return ""

win_creation()


game_win.mainloop()