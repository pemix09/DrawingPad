from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Buttons:

    def GetSaveButton(self):
        saveButton = Button(text='Save', size_hint=(0.1,0.1))
        return saveButton

    def GetLoadButton(self):
        loadButton = Button(text="Load", size_hint=(0.1,0.1))
        return loadButton

    def GetClearButton(self):
        clearButton = Button(text="Clear", size_hint=(0.1,0.1))
        return clearButton

    def GetRectangleButton(self):
        rectangleButton = Button(text="Rectangle", size_hint=(0.1,0.1))
        return rectangleButton

    def GetCircleButton(self):
        circleButton = Button(text="Circle", size_hint=(0.1, 0.1))
        return circleButton

    def GetTextButton(self):
        textButton = Button(text="Text", size_hint=(0.1, 0.1))
        return textButton

    def GetTextInput(self):
        textInput = TextInput(size_hint=(0.3, 0.1), multiline=False)
        return textInput