"""This module run calculating the balance of goods and profit take parametres from class Goods."""
from decimal import Decimal


class Goods:
    """This class describes operations taking into account the goods in the store."""

    def __init__(self, purchased_price, selling_price, volume_of_purchase_goods, volume_of_sold_goods):
        """Initialize class Goods and arguments of the class."""
        self.purchased_price = purchased_price
        self.selling_price = selling_price
        self.volume_of_purchase_goods = volume_of_purchase_goods
        self.volume_of_sold_goods = volume_of_sold_goods

    def balance_of_goods(self):
        """Calculate of the balance for the goods."""
        result = int(self.volume_of_purchase_goods - self.volume_of_sold_goods)
        return result

    def profit_of_certain_goods(self):
        """Calculate profit per product."""
        profit = (self.selling_price - self.purchased_price) * self.volume_of_sold_goods
        result = Decimal(profit).quantize(Decimal('1.00'))
        return result
