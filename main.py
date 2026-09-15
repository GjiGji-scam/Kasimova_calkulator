"""
Калькулятор в стиле iOS для Android.
Собирается через Buildozer + GitHub Actions.
"""

import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Настройка окна: тёмный фон, портретная ориентация
Window.clearcolor = (0.0, 0.0, 0.0, 1.0)


class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Главный вертикальный контейнер
        main_layout = BoxLayout(orientation="vertical", padding=[10, 10, 10, 10], spacing=10)

        # Экран калькулятора (текстовое поле)
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=75,
            foreground_color=[1, 1, 1, 1],
            background_color=[0.2, 0.2, 0.2, 1],
            cursor_color=[1, 1, 1, 1],
        )
        self.solution.bind(on_double_tap=self.on_double_tap)
        main_layout.add_widget(self.solution)

        # Раскладка кнопок (как у iOS)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                # Цвет фона для разных типов кнопок
                if label in self.operators:
                    bg_color = [1.0, 0.58, 0.0, 1]  # оранжевый (операции)
                elif label == "C":
                    bg_color = [0.6, 0.6, 0.6, 1]  # серый (очистка)
                else:
                    bg_color = [0.3, 0.3, 0.3, 1]  # тёмно-серый (цифры)

                button = Button(
                    text=label,
                    font_size=40,
                    background_normal="",
                    background_color=bg_color,
                    color=[1, 1, 1, 1],
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # Кнопка "=" отдельно, на всю ширину
        equals_button = Button(
            text="=",
            font_size=40,
            background_normal="",
            background_color=[1.0, 0.58, 0.0, 1],
            color=[1, 1, 1, 1],
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_double_tap(self, instance):
        """Двойной тап по экрану — выделить весь текст (не обязательно)."""
        self.solution.select_all()

    def on_button_press(self, instance):
        """Обработка нажатий на цифры и операторы."""
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистить всё
            self.solution.text = ""
            self.last_was_operator = False
            return

        if current and (self.last_was_operator and button_text in self.operators):
            # Нельзя ставить два оператора подряд
            return
        elif current == "" and button_text in self.operators:
            # Нельзя начинать с оператора
            return

        new_text = current + button_text
        self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        """Вычисление результата."""
        text = self.solution.text
        if not text:
            return

        # Заменяем символы для eval
        text = text.replace("÷", "/").replace("×", "*")

        # Проверка: разрешены только цифры и операторы
        if not re.match(r"^[\d+\-*/.]+$", text):
            self.solution.text = "Error"
            return

        try:
            result = str(eval(text))
            self.solution.text = result
        except ZeroDivisionError:
            self.solution.text = "Error"
        except Exception:
            self.solution.text = "Error"

        self.last_was_operator = False


if __name__ == "__main__":
    CalculatorApp().run()