import unittest

from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def testNegativeAmountThrowsException(self):
        with self.assertRaises(ValueError):
            Money(-5, "USD")

    def testMultiplicationinDollars(self):
        fiveDollars = Money(5, "USD")
        fifteenDollars = Money(15, "USD")
        self.assertEqual(fifteenDollars, fiveDollars.times(3))

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twohundretfiftyEuros = Money(250, "EUR")
        self.assertEqual(twohundretfiftyEuros, tenEuros.times(25))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMOneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMOneyAfterDivision, actualMoneyAfterDivision)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testRemove(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars, fifteenDollars)
        portfolio.remove(fifteenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testRemoveNonPortfolioItemRaisesException(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        with self.assertRaises(ValueError):
            portfolio.remove(fifteenDollars)

    def testAdditionDollarsandEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(
            expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue)
        )

    def testAdditionDollarsAndWons(self):
        oneDollar = Money(1, "USD")
        elevenHundretWon = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundretWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portfolio.evaluate("KRW")
        self.assertEqual(
            expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue)
        )

    def testAdditionDollarEurWon(self):
        twoDollars = Money(2, "USD")
        elevenHundretWon = Money(1100, "KRW")
        hundretEUR = Money(100, "EUR")
        portfolio = Portfolio()
        portfolio.add(twoDollars, elevenHundretWon, hundretEUR)
        expectedValue = Money(137700, "KRW")
        actualValue = portfolio.evaluate("KRW")
        self.assertEqual(
            expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue)
        )


if __name__ == "__main__":
    unittest.main()
