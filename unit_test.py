import time
import unittest
from utils import SimpleStockMarket
import random


class TestSum(unittest.TestCase):

    def test_dividend_yield(self):
        stock_symbol = random.choice(["TEA", "POP", "ALE", "GIN", "JOE"])
        price = random.randint(10, 1000)
        self.assertTrue(SimpleStockMarket.calculate_dividend(price, stock_symbol))

    def test_pe_ratio(self):
        stock_symbol = random.choice(["TEA", "POP", "ALE", "GIN", "JOE"])
        price = random.randint(10, 1000)
        self.assertTrue(SimpleStockMarket().pe_ratio(price, stock_symbol))

    def test_create_record(self):
        price = str(random.randint(10, 1000))
        quantity = str(random.randint(10, 500))
        action = str(random.choice(["Buy", "Sale"]))
        self.assertTrue(SimpleStockMarket.create_record(str(time.time()), quantity, action, price))

    def test_weighted_stock_within_five_minutes(self):
        self.assertTrue(SimpleStockMarket.weighted_stock_within_five_minutes())

    def test_geometry_mean_of_share_index(self):
        self.assertTrue(SimpleStockMarket.geometry_mean_of_share_index())


if __name__ == '__main__':
    unittest.main()
