from dateutil.parser import parse
from datetime import datetime
"""
Function 'authors()' open the .txt file with dates and other information 
and return list of dictionaries with original text date and modified date (dd/mm/yyyy).
"""


def authors(file_name):
    with open(file_name) as file:
        file_list = [line.strip('\n') for line in file.readlines()]
        info_list = [elem.split() for elem in file_list if len(elem.split()) > 1]
        dates = [' '.join(elem[0:3]) for elem in info_list]
        new_dates = [(parse(date)).strftime("%d/%m/%Y") for date in dates]
        dict_list = []
        for orig_dates, modified_dates in zip(dates, new_dates):
            date_dict = {'original_date': orig_dates, 'date_modified': modified_dates}
            dict_list.append(date_dict)
    return dict_list


def authors_v_2(file_name):
    with open(file_name) as file:
        file_list = [line.strip('\n') for line in file.readlines()]
        info_list = [elem.split() for elem in file_list if len(elem.split()) > 1]
        dates = [' '.join(elem[0:3]) for elem in info_list]
        new_dates = []
        dict_list = []
        for elem in dates:
            day, month, year = elem.split()
            day = day[:-2].rjust(2, '0')
            date_without_suffix = ' '.join([day, month, year])
            new_dates.append(datetime.strptime(date_without_suffix, "%d %B %Y").strftime("%d/%m/%Y"))
        for orig_dates, modified_dates in zip(dates, new_dates):
            dict_list.append({'original_date': orig_dates, 'date_modified': modified_dates})
    return dict_list


if __name__ == '__main__':
    print(authors('authors.txt'))
    print(authors_v_2('authors.txt'))
