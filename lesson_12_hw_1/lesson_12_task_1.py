"""
Function 'domains()' open the .txt file with domain names and return the list of domain names.
"""


def domains(file_name):
    with open(file_name) as file:
        domains_list = [line.strip('. \n') for line in file.readlines()]
    return domains_list


if __name__ == '__main__':
    print(domains('domains.txt'))