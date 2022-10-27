"""This module has unittests for class Program."""

import unittest
from ..classes.work_with_data import ShowBalanceProfit, WorkWithData


input_data = [{'name_of_goods': 'хлеб',
               'purchased_price': '1,5',
               'selling_price': '2,2',
               'volume_of_purchase_goods': '75',
               'volume_of_sold_goods': '25'
               },
              {'name_of_goods': 'масло',
               'purchased_price': '1,8',
               'selling_price': '2,3',
               'volume_of_purchase_goods': '10',
               'volume_of_sold_goods': '6'
               }]
work_with_data = WorkWithData(input_data)
show_balance_profit = ShowBalanceProfit(input_data, 'хлеб')


class ShowNamesTestCase(unittest.TestCase):
    """Unittest for method show_names."""

    def test_result(self):
        """Run the test."""
        expected_result = 'В базе данных есть такие товары:\nхлеб, масло'
        self.assertEqual(work_with_data.show_names(), expected_result)


class ShowTotalProfitTestCase(unittest.TestCase):
    """Unittest for method show_total_profit."""

    def test_result(self):
        """Run the test."""
        expected_result = 'Прибыль по всему магазину составляет 20.50 грн.'
        self.assertEqual(work_with_data.show_total_profit(), expected_result)


class ShowBalanceTestCase(unittest.TestCase):
    """Unittest for method show_balance."""

    def test_result(self):
        """Run the test."""
        expected_result = 'Остаток по товару хлеб составляет 50 ед.'
        self.assertEqual(show_balance_profit.show_balance(), expected_result)


class ShowProfitTestCase(unittest.TestCase):
    """Unittest for method show_profit."""

    def test_result(self):
        """Run the test."""
        expected_result = 'Прибыль по товару хлеб составляет 17.50 грн.'
        self.assertEqual(show_balance_profit.show_profit(), expected_result)
