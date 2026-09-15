# ui.py
"""Внешний вид калькулятора."""
import tkinter as tk
import settings


def create_window():
    """Создаёт главное окно."""
    root = tk.Tk()
    root.title("Калькулятор")
    root.geometry(f"{settings.WINDOW_W}x{settings.WINDOW_H}")
    root.configure(bg=settings.BG_COLOR)
    root.resizable(False, False)
    return root


def create_display(root):
    """Создаёт экран калькулятора."""
    display = tk.Label(
        root,
        text="0",
        anchor="e",
        bg=settings.DISPLAY_BG,
        fg=settings.DISPLAY_FG,
        font=settings.DISPLAY_FONT,
        padx=15,
        pady=15,
    )
    display.pack(fill="x", padx=10, pady=10)
    return display


def button_style(label):
    """Возвращает цвета для кнопки в зависимости от её типа."""
    if label in {"=", "C", "±", "%", "⌫"}:
        return settings.YELLOW, "#000000"          # жёлтый фон, чёрный текст
    if label in settings.OPERATORS:
        return settings.PURPLE, settings.WHITE     # фиолетовый фон, белый текст
    return settings.PURPLE_DARK, settings.WHITE    # тёмно-фиолетовый, белый текст


def create_buttons(root, on_click):
    """Создаёт сетку кнопок."""
    frame = tk.Frame(root, bg=settings.BG_COLOR)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    for r, row in enumerate(settings.BUTTONS):
        for c, label in enumerate(row):
            bg, fg = button_style(label)
            btn = tk.Button(
                frame,
                text=label,
                font=settings.BTN_FONT,
                bg=bg,
                fg=fg,
                activebackground=settings.YELLOW,
                activeforeground="#000000",
                bd=2,
                relief="ridge",
                command=lambda l=label: on_click(l),
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

    # растягиваем ячейки равномерно
    for i in range(4):
        frame.grid_columnconfigure(i, weight=1)
    for i in range(len(settings.BUTTONS)):
        frame.grid_rowconfigure(i, weight=1)

    return frame