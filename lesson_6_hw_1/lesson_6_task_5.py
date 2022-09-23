amount = float(input('Please, enter how many kg of wheat rajah have to give you:'))
grains = amount/0.000035
grains_list = [int(2**i) for i in range(64)]
chess_cell_list = []
numbers = range(1, 9)
letters = range(97, 105)
for let in letters:
    for num in numbers:
        chess = f'{chr(let)}{num}'
        chess_cell_list.append(chess)
for index, n in enumerate(grains_list):
    if grains <= n:
        print('Wheat chess position is:', chess_cell_list[index])
        break
