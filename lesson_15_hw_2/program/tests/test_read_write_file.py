"""This module has unittests for Class OpenWriteFile"""

import unittest
from ..classes.read_write_file import OpenWriteFile

FILE = 'товары_тест.csv'
program = OpenWriteFile(FILE)


class OpenFileTestCase(unittest.TestCase):
    """Unittest for method show_names."""

    def test_result(self):
        """Run the test."""
        expected_result = [{'name_of_goods': 'хлеб',
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
        self.assertEqual(program.open_file(), expected_result)
