from kivy.storage.jsonstore import JsonStore
from Canvas import canvas

class FileSerializer:

    def __init__(self, _filename):
        self.store = JsonStore(_filename)
        self.canvasKey = 'Canvas'

    def SaveCanvas(self):
        if canvas != '':
            self.store.put(self.canvasKey + 'X', canvas.x)
            self.store.put(self.canvasKey + "Y", canvas.y)

    def LoadCanvas(self):
        if self.store.exists(self.canvasKey):
            canvasX = self.store.get(self.canvasKey + 'X')
            canvasY = self.store.get(self.canvasKey + 'Y')
            return canvasX, canvasY
