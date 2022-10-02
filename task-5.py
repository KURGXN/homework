print('Задача 5. Кино')


def film_finder():
    film_name = input('Введите название фильма: ')
    for film in films_list:
        if film == film_name:
            favorite_list.append(film)
            return
    print('Ошибка: фильма', film_name, 'у нас нет :(')


films_list = ['\nКрепкий орешек', 'Назад в будущее', 'Таксист',
              'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
count = int(input('\nСколько фильмов хотите добавить? '))
favorite_list = []
separator = ', '

for _ in range(count):
    film_finder()

print('\nВаш список любимых фильмов:', separator.join(favorite_list))
