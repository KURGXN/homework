print('Задача 1. Текстовый редактор: возвращение')

word_list = list(input('\nВведите строку:\n'))
new_word = ''
replacement = 0

for symbol in word_list:
    if symbol == ':':
        new_word += ';'
        replacement += 1
    else:
        new_word += symbol

print('\nИсправленная строка:\n', new_word, '\n\nКол-во замен:', replacement)