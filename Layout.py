from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from ButtonCollection import Buttons
from Canvas import Canvas
buttonsCollection = Buttons()


class Layout(App):

    def build(self):
        mainLayout = BoxLayout(orientation='vertical')

        canvas = Canvas()
        buttons = BoxLayout()

        #Add elements to window
        mainLayout.add_widget(canvas)
        mainLayout.add_widget(buttons)

        #get buttons from buttons collection
        saveButton = buttonsCollection.GetSaveButton()
        loadButton = buttonsCollection.GetLoadButton()

        #Add buttons to buttons panel
        buttons.add_widget(saveButton)
        buttons.add_widget(loadButton)

        return mainLayout
