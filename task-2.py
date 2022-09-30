print('Задача 2. Соседи')

word_list = list(input('\nВведите строку: '))
sym_number = int(input('Номер символа: '))

print('\nСимвол слева:', word_list[sym_number - 2], '\nСимвол справа:', word_list[sym_number])

if word_list[sym_number - 1] == word_list[sym_number - 2] and word_list[sym_number - 1] == word_list[sym_number]:
    print('\nЕсть два таких же символа.')
elif word_list[sym_number - 1] == word_list[sym_number - 2] or word_list[sym_number - 1] == word_list[sym_number]:
    print('\nЕсть ровно один такой же символ.')
else:
    print('\nТаких же символов нет.')
