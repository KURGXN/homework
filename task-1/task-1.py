print('Задача 1. Таблица степеней')

numbers = [3,7,5]

while True:
    new_number = input('\nНовое число: ')
    if new_number == 'Секретное слово':
        print('Введено секретное слово...')
        break
    numbers.append(int(new_number))
    print('Текущий список чисел:', numbers, '\n')
    for number in numbers:
        print(number ** 2, number ** 3, number ** 4)