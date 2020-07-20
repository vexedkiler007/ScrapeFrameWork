class SaveFactory:
    factories = {}

    def addFactory(id, saveFactory):
        SaveFactory.factories.put[id] = saveFactory

    addFactory = staticmethod(addFactory)

    def createSave(id):
        if not id in SaveFactory.factories.keys():
            SaveFactory.factories[id] = eval(id + ".Factory()")

        return SaveFactory.factories[id].create()

    createSave = staticmethod(createSave)


class Save(object): pass


class SaveTextHTML(Save):
    def __init__(self, bytes_, file_name):
        self.bytes_ = bytes_
        self.file_name = file_name

    def async_save(self): print(f"saved: {self.bytes_} {self.file_name}")

    class Factory:
        def create(self): return SaveTextHTML


class SaveTextDataBase:
    def __init__(self, cols_name, rows):
        self.cols_name = cols_name
        self.rows = rows

        def async_save(self): print(f"saved: {self.bytes_} {self.file_name}")

        class Factory:
            def create(self): return SaveTextDataBase

class SaveImages: pass
class SaveVideos: pass



SaveText_obj = SaveFactory.createSave("SaveTextHTML")('cool', 'cool')
SaveText_obj.async_save()
