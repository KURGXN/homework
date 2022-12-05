# TODO Задача 1 - Список чётных чисел

user_name = input('\nВведите имя пользователя: ')
file_name = input('Введите имя файла: ')
path = 'C/{0}/docs/folder/{1}.txt'.format(
    user_name,
    file_name
)

print(f'\nПуть к файлу: {path}')
