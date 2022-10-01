print('Задача 3. Клетки')

cells_count = int(input('\nКоличество клеток: '))
wrong_cells = ''
print()

for cell in range(cells_count):
    efficiency = int(input(f'Эффективность {cell + 1} клетки: '))
    if efficiency < cell:
        wrong_cells += str(efficiency) + ' '

print('\nНеподходящие значения:', wrong_cells)
