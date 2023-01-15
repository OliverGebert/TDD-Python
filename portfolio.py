import functools
import operator

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def __convert(self, aMoney, aCurrency):
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100, "EUR->KRW": 1344}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency + "->" + aCurrency
            return aMoney.amount * exchangeRates[key]

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def remove(self, moneys):
        if moneys not in self.moneys:
            raise ValueError("money item not in portfolio")
        self.moneys.remove(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
        )
        return Money(total, currency)
