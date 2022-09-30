"""Task 3(a) original_list_a sorted sorted by element number value."""

original_list_a = [5, '9', 15, '0', 6.5, '6', 775, 2]
sorted_list_a = sorted(original_list_a, key=float)
print('First list:', original_list_a)
print('Sorted first list:', sorted_list_a)

"""Task 3(b) original_list_b sorted by the value of the first digit of the number"""

original_list_b = [42, 326, 1, '1234567', 9, '20', 2, '999']
sorted_list_b = sorted(original_list_b, key=lambda string: str(string)[:1])
print('Second list:', original_list_b)
print('Sorted second list:', sorted_list_b)
