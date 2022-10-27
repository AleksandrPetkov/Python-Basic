"""This module run the work of program operations."""
from ..classes.goods import Goods


class WorkWithData:
    """This class describe the program operations work inside."""

    def __init__(self, data_list):
        """Initialize class WorkWithData with arguments. Argument is data_list."""
        self.data_list = data_list

    def make_input_info(self):
        """Open the csv file and returns the necessary construct for the program to work."""
        names_list = []
        info_list = []
        result = {}
        for elem in self.data_list:
            dict_info = {}
            for key, item in elem.items():
                if key == 'name_of_goods':
                    names_list.append(item)
                else:
                    dict_info[key] = float(item.replace(',', '.'))
            info_list.append(dict_info)
        for name, info in zip(names_list, info_list):
            result[name] = info
        return result

    def make_goods_names(self):
        """Create a list of product names by opening the csv data file."""
        names_list = []
        for row in self.data_list:
            names_list.append(row['name_of_goods'])
        result = names_list
        return result

    def show_names(self):
        """Display all product names."""
        show_names = ', '.join(self.make_goods_names())
        result = f'В базе данных есть такие товары:\n' \
                 f'{show_names}'
        return result

    def show_total_profit(self):
        """Display profit for all products."""
        goods_dict = self.make_input_info()
        profit_list = []
        for info_dict in goods_dict.values():
            x = Goods(**info_dict)
            profit = x.profit_of_certain_goods()
            profit_list.append(profit)
        total_profit = sum(profit_list)
        result = f'Прибыль по всему магазину составляет {total_profit} грн.'
        return result


class ShowBalanceProfit(WorkWithData):
    """This class is a child class of class WorkWithData.

    And it input additional argument 'name of goods' to run class Goods.
    """

    def __init__(self, data_list, goods_name):
        """Initialize child class ShowBalanceProfit with arguments.

        Arguments are csv file and goods name.
        """
        super().__init__(data_list)
        self.goods_name = goods_name

    def show_balance(self):
        """Display the balance of the product."""
        goods_dict = self.make_input_info()
        balance = Goods(**goods_dict[self.goods_name]).balance_of_goods()
        result = f'Остаток по товару {self.goods_name} составляет {balance} ед.'
        return result

    def show_profit(self):
        """Display product profit."""
        goods_dict = self.make_input_info()
        balance = Goods(**goods_dict[self.goods_name]).profit_of_certain_goods()
        result = f'Прибыль по товару {self.goods_name} составляет {balance} грн.'
        return result
