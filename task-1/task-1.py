print('Задача 1. Гугл')

nums_list = []
nums_count = int(input('\nКол-во чисел в списке: '))

for _ in range(nums_count):
    new_num = int(input('Введите число: '))
    nums_list.append(new_num)

print('\nМаксимальное число в списке:', max(nums_list))
print('Минимальное число в списке:', min(nums_list))
