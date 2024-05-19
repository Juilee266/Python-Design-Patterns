from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def apply_discount(self, value):
        pass

class OnSaleDiscount(Strategy):
    def apply_discount(self, value):
        return value - (value*0.3)


class TwentyPercentDiscount(Strategy):
    def apply_discount(self, value):
        return value - (value * 0.2)

class Item:
    def __init__(self, discount_strategy, price):
        self.price = price
        self.discount_strategy = discount_strategy

    def get_discounted_price(self):
        return self.discount_strategy.apply_discount(self.price)

if __name__ == "__main__":
    onsale_strat = OnSaleDiscount()
    twentyp_strat = TwentyPercentDiscount()

    item1 = Item(onsale_strat, 100)
    item2 = Item(twentyp_strat, 1000)

    print("item1 discounted price =", item1.get_discounted_price())
    print("item2 discounted price =", item2.get_discounted_price())
