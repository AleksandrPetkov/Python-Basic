from dateutil.parser import parse
from datetime import datetime
"""
Function 'authors()' open the .txt file with dates and other information 
and return list of dictionaries with original text date and modified date (dd/mm/yyyy).
"""


def authors(arg):
    open_file = open(arg, 'r')
    str_list = [str_elem.split() for str_elem in open_file if '-' in str_elem]
    dates = [' '.join(elem[0:3]) for elem in str_list]
    new_dates = []
    dict_list = []
    for date in dates:
        new_date = parse(date)
        new_dates.append(new_date.strftime("%d/%m/%Y"))
    for orig_dates in dates:
        d = {'original_date': orig_dates}
        dict_list.append(d)
    for i, d in enumerate(dict_list):
        d['date_modified'] = new_dates[i]
    return dict_list


def authors_v_2(arg):
    open_file = open(arg, 'r')
    str_list = [str_elem.split() for str_elem in open_file if '-' in str_elem]
    dates = [' '.join(elem[0:3]) for elem in str_list]
    new_dates = []
    modified_dates = []
    dict_list = []
    for orig_dates in dates:
        d = {'original_date': orig_dates}
        dict_list.append(d)
        new_dates.append(orig_dates.split())
    for elem in new_dates:
        elem[0] = elem[0][:-2]
        if int(elem[0]) < 10:
            elem[0] = '0' + elem[0]
        elem2 = ' '.join(elem)
        modified_dates.append((datetime.strptime(elem2, "%d %B %Y")).strftime("%d/%m/%Y"))
    for i, d in enumerate(dict_list):
        d['date_modified'] = modified_dates[i]
    return dict_list


def main():
    print(authors('authors.txt'))
    print(authors_v_2('authors.txt'))


if __name__ == '__main__':
    main()
