from abc import ABC, abstractmethod


class SaveAbstractClass(ABC):
    def __new__ (cls, data):
        if cls.check_format(data):
            instance = super().__new__(cls)
            print('it did work')
            return instance
        else:
            print('Boo it didn\'t work')
            return None

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def check_format(data):
        pass




class SaveText(SaveAbstractClass):

    def __init__(self, data):
        print('It worked!')

    def save(self):
        pass

    @staticmethod
    def check_format(data):
        print('test')
        return isinstance(data, tuple)




# check data before a class becomes instantiated
# check the data: match a certain format
# create check format method that creates and match or not (bool)
# typing.Protocol