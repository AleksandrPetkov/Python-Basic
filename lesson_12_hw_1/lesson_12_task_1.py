"""
Function 'domains()' open the .txt file with domain names and return the list of domain names.
"""


def domains(arg):
    open_file = open(arg, 'r')
    letter_list = []
    for line in open_file:
        for letter in line:
            if letter != '\n':
                letter_list.append(letter)
    domains_no_dots = (''.join(letter_list)).split('.')
    result = [res for res in domains_no_dots if len(res) != 0]
    return result


def main():
    print(domains('domains.txt'))


if __name__ == '__main__':
    main()
