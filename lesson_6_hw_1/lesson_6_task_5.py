amount = float(input('Please, enter how many kg of wheat rajah have to give you:'))
grains = amount//0.03584
grains_list = [int(2**(i-1)) for i in range(1, 65)]
chess_cell_list = []
numbers = range(1, 9)
letters = range(97, 105)
for let in letters:
    for num in numbers:
        chess = f'{chr(let)}{num}'
        chess_cell_list.append(chess)
for n in grains_list:
    if grains == n:
        grains_list_index = grains_list.index(n)
        print('Wheat chess position is:', chess_cell_list[grains_list_index])
        break
    if grains < n:
        grains_list_index = grains_list.index(n)
        print('Wheat chess position is:', chess_cell_list[grains_list_index])
        break
