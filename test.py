import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Таблица кнопок")

    # Создаем фрейм для кнопок 3x3
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Создаем кнопки в виде таблицы 3x3
    for row in range(3):
        for col in range(3):
            button = tk.Button(frame, text=f"Кнопка {row * 3 + col + 1}", width=10, height=3)
            button.grid(row=row, column=col, padx=5, pady=5)

    # Создаем две кнопки, занимающие всю ширину
    button_full_1 = tk.Button(root, text="Кнопка 4", width=30, height=2)
    button_full_1.pack(pady=5)

    button_full_2 = tk.Button(root, text="Кнопка 5", width=30, height=2)
    button_full_2.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
