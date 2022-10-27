"""This module has unittests for Class Goods."""
import unittest

from ..classes.goods import Goods


class BalanceOfGoodsTestCase(unittest.TestCase):
    """Unittest fo method balance_of_goods."""

    def test_result(self):
        """Run the test."""
        self.assertEqual(Goods(5, 10, 5, 2).balance_of_goods(), 3)


class ProfitOfCertainGoods(unittest.TestCase):
    """Unittest fo method balance_of_goods."""

    def test_result(self):
        """Run the test."""
        self.assertEqual(Goods(5, 10, 5, 2).profit_of_certain_goods(), 10)
