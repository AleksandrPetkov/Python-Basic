"""
Function "copydeep" make a deep copy of list with another list, tuple or dict.
"""


def copydeep(arg):
    if isinstance(arg, list):
        return list(map(copydeep, arg))
    elif isinstance(arg, tuple):
        return tuple(map(copydeep, arg))
    elif isinstance(arg, dict):
        return {
            copydeep(key): copydeep(value)
            for key, value in arg.items()
        }
    return arg


def main():
    lst_1 = ['a', 1, (2.0, 0, [75], {'a': 2, 'b': 1}), ['b'], {'a': 2, 'b': [1, 3]}]
    lst_2 = copydeep(lst_1)
    # вставка во вложенный список
    lst_1[3].append(0)
    # вставка во вложенный кортеж
    lst_1[2][2].append(3)
    lst_1[2][3]['b'] = 5
    # вставка во вложенный словарь
    lst_1[4]['b'] = 5
    print(f'Original: {lst_1}\n'
          f'Function: {lst_2}\n')


if __name__ == '__main__':
    main()
