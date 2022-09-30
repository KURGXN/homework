print('Задача 3. Улучшенная лингвистика')

words_list = []
word_count_list = [0, 0, 0]
print()

for count in range(3):
    words_list.append(input(f'Введите {count + 1} слово: '))

new_word = ''
print()

while new_word != 'end':
    new_word = input('Слово из текста: ')
    if new_word == words_list[0]:
        word_count_list[0] += 1
    elif new_word == words_list[1]:
        word_count_list[1] += 1
    elif new_word == words_list[2]:
        word_count_list[2] += 1
    elif new_word == 'end':
        break

print(f'\nПодсчёт слов в тексте')
for number in range(3):
    print(f'{words_list[number]}:{word_count_list[number]}')
