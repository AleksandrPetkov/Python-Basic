"""This module has class RunProgram. And show to user work of program."""
from ..classes.errors import ProgramError
from ..classes.read_write_file import OpenWriteFile
from ..classes.work_with_data import WorkWithData, ShowBalanceProfit


class RunProgram:
    """This class run the program and output the result of working.

    Methods: choose_operation, show_program_result.
    """

    user_choose_operation = ''

    def __init__(self, csv_file):
        """Initialize class RunProgram. Argument is csv_file."""
        self.csv_file = csv_file

    def choose_operation(self):
        """Show to user variant of program work and take the user`s choose."""
        operations_list = {'1': 'Показать список товаров',
                           '2': 'Показать остаток по товару',
                           '3': 'Показать прибыль по товару',
                           '4': 'Показать общую прибыль по магазину',
                           '5': 'Добавить новый товар'
                           }
        check_list = list(operations_list.keys())
        for key, item in operations_list.items():
            print(f'{key}-{item}')
        while True:
            answer = input('Введите номер операции:')
            if answer in check_list:
                self.user_choose_operation = answer
                return self.user_choose_operation
            else:
                ProgramError('Вы ввели неправильный номер, попробуйте еще раз.').print_error()
                continue

    def show_program_result(self):
        """Show to user the result of program works."""
        open_write_file = OpenWriteFile(self.csv_file)
        data_dict = open_write_file.open_file()
        work_with_data = WorkWithData(data_dict)
        if self.user_choose_operation in ['2', '3']:
            check_list = work_with_data.make_goods_names()
            while True:
                answer = input('Введите название товара:')
                if answer in check_list:
                    user_choose_goods = answer
                    show_balance_profit = ShowBalanceProfit(data_dict, user_choose_goods)
                    operations_list = {'2': show_balance_profit.show_balance,
                                       '3': show_balance_profit.show_profit,
                                       }
                    print(operations_list[self.user_choose_operation]())
                    break
                else:
                    ProgramError('Такого наименования нет в базе данных,'
                                 ' попробуйте еще раз.').print_error()
        else:
            operations_list = {'1': work_with_data.show_names,
                               '4': work_with_data.show_total_profit,
                               '5': open_write_file.add_new_goods
                               }
            print(operations_list[self.user_choose_operation]())
