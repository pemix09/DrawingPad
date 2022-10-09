from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from ButtonCollection import Buttons
from Canvas import Canvas
from FileSerializer import FileSerializer
buttonsCollection = Buttons()


class Layout(App):

    def build(self):
        mainLayout = BoxLayout(orientation='vertical')

        self.painter = Canvas()
        self.buttons = BoxLayout()

        #Add elements to window
        mainLayout.add_widget(self.painter)
        mainLayout.add_widget(self.buttons)

        #get buttons from buttons collection
        saveButton = buttonsCollection.GetSaveButton()
        saveButton.bind(on_press=self.save)

        loadButton = buttonsCollection.GetLoadButton()
        loadButton.bind(on_press=self.Load)

        clearButton = buttonsCollection.GetClearButton()
        clearButton.bind(on_press = self.clear)

        rectangleButton = buttonsCollection.GetRectangleButton()
        rectangleButton.bind(on_press = self.Rectangle)

        #Add buttons to buttons panel
        self.buttons.add_widget(saveButton)
        self.buttons.add_widget(loadButton)
        self.buttons.add_widget(clearButton)
        self.buttons.add_widget(rectangleButton)

        return mainLayout

    def save(self, obj):
        files = FileSerializer()

        canvas = self.painter.canvas
        files.Save(canvas)
        self.painter.export_as_image().save('image.jpg')

    def clear(self, obj):
        self.painter.canvas.clear()

    def Load(self, obj):
        image = self.painter.export_as_image().load('image.jpg')

    def Rectangle(self, obj):
        self.painter.DrawRectangle()