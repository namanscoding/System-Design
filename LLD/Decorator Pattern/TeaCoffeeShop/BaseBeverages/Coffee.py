from Beverages import Beverages

class Coffee(Beverages):

    def __init__(self,price):
        self.price = price

    def baseprice(self):
        return self.price

class Americano(Coffee):
    def __init__(self):
        super().__init__(100)

class Latte(Coffee):
    def __init__(self):
        super().__init__(120)

class Espresso(Coffee):
    def __init__(self):
        super().__init__(140)
