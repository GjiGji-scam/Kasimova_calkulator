# main.py
# Точка входа: соединяет settings.py + ui.kv + логику калькулятора

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.config import Config

import settings

# Фиксируем размер окна (для десктопа)
Config.set('graphics', 'resizable', '1')
Window.size = settings.WINDOW_SIZE
Window.title = settings.WINDOW_TITLE


class CalcRoot(BoxLayout):
    """Корневой виджет калькулятора. Логика + ссылка на ui.kv"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._draw_stars()

    # ---------- Звёзды на фоне ----------
    def _draw_stars(self):
        """Рисует случайные звёзды на чёрном фоне"""
        count = random.randint(settings.STAR_COUNT_MIN, settings.STAR_COUNT_MAX)
        w, h = Window.width, Window.height
        with self.canvas.before:
            for _ in range(count):
                x = random.uniform(0, w)
                y = random.uniform(0, h)
                size = random.uniform(settings.STAR_SIZE_MIN, settings.STAR_SIZE_MAX)
                alpha = random.uniform(0.3, 1.0)
                Color(1, 1, 1, alpha)
                Ellipse(pos=(x, y), size=(size, size))

    # ---------- Логика калькулятора ----------
    @property
    def display(self):
        return self.ids.display

    def press(self, value):
        d = self.display
        if d.text == '0' and value not in ('.', '%'):
            d.text = value
        else:
            if value == '.' and '.' in d.text.split('.')[-1] and not any(
                op in d.text for op in '+-*/%'
            ):
                return
            d.text += value

    def clear(self):
        self.display.text = '0'

    def backspace(self):
        d = self.display
        d.text = d.text[:-1] if len(d.text) > 1 else '0'

    def negate(self):
        d = self.display
        if d.text.startswith('-'):
            d.text = d.text[1:]
        elif d.text != '0':
            d.text = '-' + d.text

    def equals(self):
        d = self.display
        try:
            expr = d.text.replace('×', '*').replace('÷', '/').replace('−', '-')
            # Безопасный eval — только цифры и операторы
            allowed = set('0123456789.+-*/%() ')
            if not set(expr) <= allowed:
                raise ValueError("Недопустимые символы")
            result = eval(expr, {"__builtins__": {}}, {})
            # Красиво форматируем
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            d.text = str(result)
        except ZeroDivisionError:
            d.text = 'Деление на 0'
        except Exception:
            d.text = 'Ошибка'


class CalculatorApp(App):
    def build(self):
        # Подключаем ui.kv автоматически (Kivy ищет файл с именем класса)
        # CalcRoot -> calcroot.kv. Переименуем через Builder
        from kivy.lang import Builder
        Builder.load_file('ui.kv')
        return CalcRoot()

    def on_pause(self):
        return True  # важно для Android — не убивать при свёртывании

    def on_resume(self):
        pass


if __name__ == '__main__':
    CalculatorApp().run()