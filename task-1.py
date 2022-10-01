print('Задача 1. Генерация списка')

N = int(input('\nВведите число: '))
numbers_list = []

for number in range(1, N + 1, 2):
    numbers_list.append(number)

print('Список из нечётных чисел от одного до N:', numbers_list)
