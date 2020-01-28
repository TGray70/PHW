from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def tissueСonsumption(self):
        pass

class Coat(Clothes):
    def __init__ (self, V):
        self.V = V
    @property
    def tissueСonsumption(self):
        return self.V / 6.5 + 0.5

class Suit(Clothes):
    def __init__ (self, H):
        self.H = H
    @property
    def tissueСonsumption(self):
        return 2 * self.H + 0.3

Coat1 = Coat(5)
Suit2 = Suit(10)
s = round(Coat1.tissueСonsumption + Suit2.tissueСonsumption, 2)
print('сумарный расход ткани: ', s)







