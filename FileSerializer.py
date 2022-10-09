from kivy.storage.jsonstore import JsonStore
import json

class FileSerializer:

    def Save(self, canvas):

        jsonObject = json.dumps(canvas)

        with open("drawing.json", "w") as outfile:
            outfile.write(jsonObject)

    #
    # def SaveCanvas(self):
    #     print(canvas)
    #     if canvas != '':
    #         self.store.put(self.canvasKey + 'X', canvas.x)
    #         self.store.put(self.canvasKey + "Y", canvas.y)
    #
    # def LoadCanvas(self):
    #     print(canvas)
    #     if self.store.exists(self.canvasKey):
    #         canvasX = self.store.get(self.canvasKey + 'X')
    #         canvasY = self.store.get(self.canvasKey + 'Y')
    #         return canvasX, canvasY
