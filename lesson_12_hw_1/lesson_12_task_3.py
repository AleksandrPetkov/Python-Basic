from dateutil.parser import parse
from datetime import datetime
"""
Function 'authors()' open the .txt file with dates and other information 
and return list of dictionaries with original text date and modified date (dd/mm/yyyy).
"""


def authors(file_name):
    with open(file_name) as file:
        file_list = []
        dict_list = []
        for line in file.readlines():
            splitted_line = line.split()
            if len(splitted_line) > 1:
                file_list.append(splitted_line)
        dates = [' '.join(elem[0:3]) for elem in file_list]
        for old_dates in dates:
            new_dates = (parse(old_dates)).strftime('%d/%m/%Y')
            date_dict = {'original_date': old_dates, 'date_modified': new_dates}
            dict_list.append(date_dict)
    return dict_list


def authors_v_2(file_name):
    with open(file_name) as file:
        file_list = []
        dict_list = []
        for line in file.readlines():
            splitted_line = line.split()
            if len(splitted_line) > 1:
                file_list.append(splitted_line)
        dates = [' '.join(elem[0:3]) for elem in file_list]
        for old_dates in dates:
            day, month, year = old_dates.split()
            day = day[:-2].rjust(2, '0')
            date_without_suffix = ' '.join([day, month, year])
            new_dates = datetime.strptime(date_without_suffix, '%d %B %Y').strftime('%d/%m/%Y')
            dict_list.append({'original_date': old_dates, 'date_modified': new_dates})
    return dict_list


if __name__ == '__main__':
    print(authors('authors.txt'))
    print(authors_v_2('authors.txt'))
