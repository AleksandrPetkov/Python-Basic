"""
Function 'surname()' open the .txt file with names, surnames and other information and return only surnames in list.
"""


def surname(file_name):
    with open(file_name) as file:
        file_list = [line.strip('\n') for line in file.readlines()]
        surnames_list = [elem.split('\t')[1] for elem in file_list]
    return surnames_list


if __name__ == '__main__':
    print(surname('names.txt'))
