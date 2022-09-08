cell_one = input('Please enter the first cell, for example"d3": ')
cell_two = input('Please enter the first cell, for example"g7": ')
cells = cell_one + cell_two
x1, x2 = map(ord, cells[0::2])
y1, y2 = map(int, cells[1::2])
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print('Horse CAN get from the first cell to the second in one move.')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print('Horse CAN get from the first cell to the second in one move.')
else:
    print('Horse CANNOT get from the first cell to the second in one move.')
