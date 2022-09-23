def copydeep(lst1):
    lst2 = []
    for elem in lst1:
        if isinstance(elem, list):
            lst2.append(copydeep(elem))
        else:
            lst2.append(elem)
    return lst2


lst_1 = ['a', 1, 2.0, ['b']]
lst_2 = copydeep(lst_1)
lst_1[3].append(0)
print(lst_1, lst_2)  # ['b', 0] ['b']