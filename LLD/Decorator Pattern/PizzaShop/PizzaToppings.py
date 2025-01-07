from abc import ABC, abstractmethod
from BasePizza import basePizza
class Toppings(basePizza):

    def __init__(self, pizza):
        self.pizza = pizza

    @abstractmethod
    def getDescrption(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass


class Mushroom(Toppings):

    def __init__(self):
        super().__init__(basePizza())

    def getDescrption(self):
        return basePizza().getDescrption() + "Mushroom"

    def getPrice(self):
        return basePizza().getPrice() + 20.0

class ExtraCheese(Toppings):

    def getDescrption(self):
        return self.pizza.getDescrption() + "ExtraCheese"

    def getPrice(self):
        return self.pizza.getPrice() + 30.0

