"""
Function  "group_by_surname()" divides students into 4 groups, depending on the first letter of the surname.
"""


def group_by_surname(list_of_enrollees):
    group_a_i = []
    group_j_p = []
    group_q_t = []
    group_u_z = []
    for elem in list_of_enrollees:
        name_surname = elem.split()
        if ord(name_surname[1][0]) in range(ord('A'), ord('I')+1):
            group_a_i.append(elem)
        elif ord(name_surname[1][0]) in range(ord('J'), ord('P')+1):
            group_j_p.append(elem)
        elif ord(name_surname[1][0]) in range(ord('Q'), ord('T')+1):
            group_q_t.append(elem)
        elif ord(name_surname[1][0]) in range(ord('U'), ord('Z')+1):
            group_u_z.append(elem)
    return len(group_a_i), len(group_j_p), len(group_q_t), len(group_u_z)


def main():
    students_list = ['Mark Aarkov', 'Ann Roshen', 'Helen Stiller', 'Mary Moroy', 'Diana United']
    group_1, group_2, group_3, group_4 = group_by_surname(students_list)
    print('The list of enrolles is: ', ','.join(students_list))
    print(f'The group "A-I" consist of {group_1} students.\n'
          f'The group "J-P" consist of {group_2} students.\n'
          f'The group "Q-T" consist of {group_3} students.\n'
          f'The group "U-Z" consist of {group_4} students.')


if __name__ == '__main__':
    main()
