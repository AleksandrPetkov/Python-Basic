"""
Function 'surname()' open the .txt file with names, surnames and other information and return only surnames in list.
"""

def surname(arg):
    open_file = open(arg, 'r')
    surname_list = []
    for line in open_file:
        splitted_line = line.split('\t')
        surname_list.append(splitted_line[1])
    return surname_list


def main():
    print(surname('names.txt'))


if __name__ == '__main__':
    main()
