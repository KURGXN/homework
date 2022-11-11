numbers_count = int(input('\nКол-во чисел: '))
numbers_list = []
for _ in range(numbers_count):
    number = int(input('Число: '))
    numbers_list.append(number)

print('\nПоследоватлеьность:', numbers_list)
second_numbers_list = []
for number in numbers_list:
    second_numbers_list.insert(0, number)

while second_numbers_list[0] == numbers_list[len(numbers_list) - 1]:
    second_numbers_list.remove(second_numbers_list[0])

print('Нужно приписать чисел:', len(second_numbers_list))
print('Сами числа:', second_numbers_list)
