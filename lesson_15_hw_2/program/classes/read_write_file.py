"""This module have parent class Program and child class ShowBalanceProfit.

These classes have methods which show to user programm working.
"""
import csv
import googletrans
from ..classes.errors import ProgramError


class OpenWriteFile:
    """This class open the file and write into it."""

    def __init__(self, csv_file):
        """Initialize class OpenWriteFile with arguments. Argument is csv file."""
        self.csv_file = csv_file

    def open_file(self):
        """Open file and make data_list."""
        data_list = []
        with open(self.csv_file, encoding='cp1251') as data_file:
            data_dict = csv.DictReader(data_file, delimiter=';')
            for row in data_dict:
                data_list.append(row)
        return data_list

    def add_new_goods(self):
        """Write a new product type to a csv file."""
        translator = googletrans.Translator()
        with open(self.csv_file, 'r+', encoding='cp1251') as data_file:
            reader = csv.reader(data_file, delimiter=';')
            headers = next(reader)
            name = []
            column = []
            for elem in headers:
                if elem == 'name_of_goods':
                    name.append(elem)
                else:
                    column.append(elem)
            new_goods_info = {}
            for elem in name:
                trans_elem = translator.translate(text=elem.replace('_', ' '), dest='ru')
                answer = input(f"Введите значение для позиции '{trans_elem.text}':")
                new_goods_info[elem] = answer
            for elem in column:
                trans_elem = translator.translate(text=elem.replace('_', ' '), dest='ru')
                while True:
                    try:
                        answer = input(f"Введите значение для позиции '{trans_elem.text}':")
                        convert_answer = float(answer.replace(',', '.'))
                        if isinstance(convert_answer, float):
                            new_goods_info[elem] = str(convert_answer).replace('.', ',')
                            break
                    except Exception as _:
                        ProgramError("Введенное значение должно быть числом").print_error()
            writer = csv.DictWriter(data_file, fieldnames=headers, delimiter=';', lineterminator='\n')
            writer.writerow(new_goods_info)
            result = 'Товар успешно добавлен!'
            return result
