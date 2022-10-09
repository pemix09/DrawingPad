from kivy.uix.widget import Widget
from kivy.graphics import Line

canvas = ''

class Canvas(Widget):

    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        #using global variable
        global canvas
        canvas = touch.ud["line"].points
