from kivy.uix.button import Button
from FileSerializer import FileSerializer


class Buttons:

    def __init__(self):
        self.file = FileSerializer('DrawingPad')

    def GetSaveButton(self):
        saveButton = Button(text='Save', size_hint=(0.1,0.1))
        saveButton.bind(on_press=self.SaveButtonAction)
        return saveButton

    def SaveButtonAction(self, button):
        print('The button '+button.text+' has been clicked')
        self.file.SaveCanvas()

    def GetLoadButton(self):
        loadButton = Button(text="Load", size_hint=(0.1,0.1))
        loadButton.bind(on_press=self.LoadButtonAction)
        return loadButton

    def LoadButtonAction(self, button):
        print('The button '+button.text+' has been clicked')
        canvas = self.file.LoadCanvas()
        return canvas
