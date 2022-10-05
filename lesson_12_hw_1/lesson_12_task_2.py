"""
Function 'surname()' open the .txt file with names, surnames and other information and return only surnames in list.
"""


def surname(file_name):
    with open(file_name) as file:
        surnames_list = []
        for line in file.readlines():
            splitted_line = line.split('\t')
            surnames_list.append(splitted_line[1])
    return surnames_list


if __name__ == '__main__':
    print(surname('names.txt'))
