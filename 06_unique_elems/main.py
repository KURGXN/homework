first_list = []
second_list = []

for digit in range(3):
    first_list_digit = int(input(f'Введите {digit + 1}-е число для первого списка: '))
    first_list.append(first_list_digit)
print()
for digit in range(7):
    second_list_digit = int(input(f'Введите {digit + 1}-е число для второго списка: '))
    second_list.append(second_list_digit)

print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

for number in range(len(first_list)):
    if first_list.count(number) > 1:
        for _ in range(first_list.count(number) - 1):
            first_list.remove(number)

print('\nНовый первый список с уникальными элементами:', first_list)
