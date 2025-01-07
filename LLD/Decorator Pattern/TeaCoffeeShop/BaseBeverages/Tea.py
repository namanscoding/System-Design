from Beverages import Beverages

class Tea(Beverages):

    def __init__(self,price):
        self.price = price

    def baseprice(self):
        return self.price


class GingerTea(Tea):
    def __init__(self):
        super().__init__(70)


class ElaichiTea(Tea):
    def __init__(self):
        super().__init__(85)


class MasalaTea(Tea):
    def __init__(self):
        super().__init__(90)
