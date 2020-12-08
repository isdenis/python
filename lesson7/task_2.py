from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothes_param):
        self.clothes_param = clothes_param

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    @property
    def cloth(self):
        return f"{round((self.clothes_param / 6.5 + 0.5), 2)}"


class Suit(Clothes):
    @property
    def cloth(self):
        return f"{round((2 * self.clothes_param + 0.3), 2)}"


coat = Coat(40)
suit = Suit(200)

print(f"Суммарный расход ткани составляет: {float(coat.cloth) + float(suit.cloth)}")
