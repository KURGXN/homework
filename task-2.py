print('Задача 2. Кратность')

nums_list = []
nums_count = int(input('\nКол-во чисел в списке: '))

for place in range(nums_count):
    number = int(input(f'Введите {place + 1} число: '))
    nums_list.append(number)

divider = int(input('\nВведите делитель: '))
print()
num_index = 0
index_sum = 0

for number in nums_list:
    if number % divider == 0:
        print(f'Индекс числа {number}: ', num_index)
        index_sum += num_index
    num_index += 1

print('Сумма индексов:', index_sum)
