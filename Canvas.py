from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.uix.gridlayout import GridLayout

class Canvas(Widget):

    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        self.figures = []
        self.selectedFigure = None
        self.textInput=''

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

        for figure in self.figures:
            fig_start = figure.pos
            fig_end = (figure.pos[0] + figure.size[0],figure.pos[1] + figure.size[1])
            mouse_pos = self.to_local(*touch.pos)
            if fig_start < mouse_pos and fig_end > mouse_pos:
                with self.canvas:
                    print('XD')#TODO
                    self.selectedFigure = figure

    def on_touch_move(self, touch):
        if len(self.figures) == 0:
            touch.ud["line"].points += (touch.x, touch.y)

        for figure in self.figures:
            fig_start = figure.pos
            fig_end = (figure.pos[0] + figure.size[0],figure.pos[1] + figure.size[1])
            mouse_pos = self.to_local(*touch.pos)
            if fig_start < mouse_pos and fig_end > mouse_pos:
                figure.pos = (mouse_pos[0] - figure.size[0]/2,mouse_pos[1] - figure.size[1]/2)
            elif fig_start == mouse_pos or fig_end == mouse_pos:
                print('Im holding something')
                #TODO!
            else:
                touch.ud["line"].points += (touch.x, touch.y)
    def DrawRectangle(self, button):
        with self.canvas:
            self.figures.append(Rectangle(pos=(0,0), size=(50,50)))

    def DrawCircle(self, button):
        with self.canvas:
            self.figures.append(Ellipse(pos=(0,0)))

    def EditFigure(self, obj):
        with self.canvas:
            print(obj.text)