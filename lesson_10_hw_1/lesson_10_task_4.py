"""
Function  "group_by_surname()" divides students into 4 groups, depending on the first letter of the surname.
"""


def group_by_surname(list_of_enrollees):
    group_a_i = []
    group_j_p = []
    group_q_t = []
    group_u_z = []
    index = 0
    while index < len(list_of_enrollees):
        elem = list_of_enrollees[index]
        name, surname = elem.split()
        if 'A' <= surname[0] <= 'I':
            group_a_i.append(elem)
        elif 'J' <= surname[0] <= 'P':
            group_j_p.append(elem)
        elif 'Q' <= surname[0] <= 'T':
            group_q_t.append(elem)
        elif 'U' <= surname[0] <= 'Z':
            group_u_z.append(elem)
        index += 1
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
