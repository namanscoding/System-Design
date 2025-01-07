from abc import ABC, abstractmethod

class Beverages(ABC):

    @abstractmethod
    def basePrice(self):
        pass