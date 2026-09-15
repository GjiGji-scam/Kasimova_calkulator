# main.py
"""Логика калькулятора и точка входа."""
import ui


class Calculator:
    def __init__(self):
        self.current = "0"
        self.previous = None
        self.operator = None
        self.reset_next = False

        self.root = ui.create_window()
        self.display = ui.create_display(self.root)
        ui.create_buttons(self.root, self.on_button)

    def update(self):
        self.display.config(text=self.current)

    def on_button(self, label):
        try:
            if label.isdigit():
                if self.reset_next or self.current == "0":
                    self.current = label
                    self.reset_next = False
                else:
                    self.current += label

            elif label == ".":
                if "." not in self.current:
                    self.current += "."

            elif label == "C":
                self.current = "0"
                self.previous = None
                self.operator = None
                self.reset_next = False

            elif label == "±":
                self.current = self.current[1:] if self.current.startswith("-") else "-" + self.current

            elif label == "%":
                self.current = str(float(self.current) / 100)

            elif label == "⌫":
                self.current = self.current[:-1] or "0"

            elif label in {"+", "−", "×", "÷"}:
                if self.operator and not self.reset_next:
                    self.calculate()
                self.previous = float(self.current)
                self.operator = label
                self.reset_next = True

            elif label == "=":
                self.calculate()
                self.operator = None
                self.previous = None

        except Exception:
            self.current = "Ошибка"

        self.update()

    def calculate(self):
        if self.operator is None or self.previous is None:
            return
        cur = float(self.current)
        if self.operator == "+":
            result = self.previous + cur
        elif self.operator == "−":
            result = self.previous - cur
        elif self.operator == "×":
            result = self.previous * cur
        else:  # ÷
            result = self.previous / cur if cur != 0 else float("nan")

        if result != result:  # NaN
            self.current = "Ошибка"
        elif result == int(result):
            self.current = str(int(result))
        else:
            self.current = str(round(result, 10))

        self.previous = result
        self.reset_next = True

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Calculator().run()