from collections.abc import Iterable
import itertools

"""
Function "lchain" takes many iterables objects and return the list with elements of all objects from function argument,
using isinstansee() function and class Iterable from collections.abc
"""


def lchain(*iterables):
    result = []
    for elem in iterables:
        if isinstance(elem, Iterable):
            for part in elem:
                result.append(part)
    return result


"""
Function "lchain_1" takes many iterables objects and return the list with elements of all objects from 
function argument, using iter() function
"""


def lchain_1(*iterables):
    result = []
    for elem in iterables:
        for part in iter(elem):
            result.append(part)
    return result


"""
Function "lchain_2" takes many iterables objects and return the list with elements of all objects from 
function argument, using chain() function from itertools module
"""


def lchain_2(*iterables):
    result = list(itertools.chain(*iterables))
    return result


def test_lchain():
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


def main():
   print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
   print(lchain_1([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
   print(lchain_2([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))


if __name__ == '__main__':
    test_lchain()
    main()



