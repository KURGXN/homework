print('Задача 1. Гугл')

nums_list = []

for _ in range(int(input('\nКол-во чисел в списке: '))):
    nums_list.append(int(input('Введите число: ')))

print('\nМаксимальное число в списке:', max(nums_list))
print('Минимальное число в списке:', min(nums_list))
