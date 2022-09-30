"""
Function "index(lst, elem)" define the index of certain element in user list and return None,
if element isn`t in list.
"""


def index(lst, elem):
    for idx, num in enumerate(lst):
        if num == elem:
            return idx


def test_index():
    assert index([1, 5, 'd', 6, 2.5], 6) == 3
    assert index([1, 5, 'd', 6, 2.5], 'a') is None


def main():
    print(index([2, 5, 2.5, 'h', 6], 8))
    print(index([2, 3.33, 9, 'c', 6], 3.33))
    print(index([2, 'e', 3, 7, 'k'], 'k'))


if __name__ == "__main__":
    test_index()
    main()
