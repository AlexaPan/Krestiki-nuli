import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Таблица надписей с кнопками")

    # Создаем фрейм для надписей 3x3
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Создаем метки в виде таблицы 3x3
    for row in range(3):
        for col in range(3):
            label = tk.Label(frame, text=f"Надпись {row * 3 + col + 1}", width=10, height=3, borderwidth=1, relief="solid")
            label.grid(row=row, column=col, padx=5, pady=5)

    # Создаем метки, занимающие всю ширину
    label_full_1 = tk.Label(frame, text="Надпись 4", width=30, height=2, borderwidth=1, relief="solid")
    label_full_1.grid(row=3, column=0, columnspan=3, pady=5)

    label_full_2 = tk.Label(frame, text="Надпись 5", width=30, height=2, borderwidth=1, relief="solid")
    label_full_2.grid(row=4, column=0, columnspan=3, pady=5)

    # Создаем фрейм для кнопок
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Создаем две кнопки, одну под другой
    button_1 = tk.Button(button_frame, text="Кнопка 1", width=15, height=2)
    button_1.pack(pady=5)

    button_2 = tk.Button(button_frame, text="Кнопка 2", width=15, height=2)
    button_2.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
