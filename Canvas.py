from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.graphics import Color

class Canvas(Widget):

    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        self.figures = []

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)

    def DrawRectangle(self):
        with self.canvas:
            self.figures.append(Rectangle(pos=(0,0), size=(50,50)))