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
        rectangleButton.bind(on_press = self.painter.DrawRectangle)

        circleButton = buttonsCollection.GetCircleButton()
        circleButton.bind(on_press = self.painter.DrawCircle)

        textInput = buttonsCollection.GetTextInput()
        textInput.bind(on_text_validate=self.on_enter_input_text)

        #Add buttons to buttons panel
        self.buttons.add_widget(saveButton)
        self.buttons.add_widget(loadButton)
        self.buttons.add_widget(clearButton)
        self.buttons.add_widget(rectangleButton)
        self.buttons.add_widget(circleButton)
        self.buttons.add_widget(textInput)

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

    def on_enter_input_text(self, obj):
        if self.painter.selectedFigure != None:
            self.painter.EditFigure(obj)
        elif obj.text == 'circle':
            self.painter.DrawCircle(obj)
        elif obj.text == 'square':
            self.painter.DrawRectangle(obj)