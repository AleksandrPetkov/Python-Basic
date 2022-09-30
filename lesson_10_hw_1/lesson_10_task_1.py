"""
Function "copydeep" make a deep copy of list with another list, tuple or dict.
"""


def copydeep(arg):
    list_copy_deep = []
    for elem in arg:
        if isinstance(elem, list):
            list_copy_deep.append(copydeep(elem))
        elif isinstance(elem, tuple):
            tpl2 = tuple(copydeep(elem))
            list_copy_deep.append(tpl2)
        elif isinstance(elem, dict):
            dict_1 = {}
            for key in elem:
                dict_1[key] = elem[key]
            list_copy_deep.append(dict_1)
        else:
            list_copy_deep.append(elem)
    return list_copy_deep

lst_1 = ['a', 1, (2.0, 0, [75], {'a':2, 'b':1}), ['b'], {'a':2, 'b':1}]
lst_2 = copydeep(lst_1)
#вставка во вложенный список
lst_1[3].append(0)
#вставка во вложенный кортеж
lst_1[2][2].append(3)
lst_1[2][3]['c'] = 5
#вставка во вложенный словарь
lst_1[4]['D'] = 5

print(f'Original: {lst_1}\n'
      f'Function: {lst_2}\n')
