from abc import ABC, abstractmethod

class basePizza(ABC):

    @abstractmethod
    def getDescrption(self):
        pass
    @abstractmethod
    def getPrice(self):
        pass

class farmHouse(basePizza):

    def getDescrption(self):
        return "FarmHouse"

    def getPrice(self):
        return 100.0


class Margherita(basePizza):

    def getDescrption(self):
        return "Margherita"

    def getPrice(self):
        return 80.0

