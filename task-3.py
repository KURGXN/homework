print('Задача 3. Собачьи бега')

points_list = []

dogs_count = int(input('\nКол-во собак, участвующих в забеге: '))
print()

for dog in range(1, dogs_count + 1):
    dog_points = float(input(f'Кол-во очков у {dog} собаки: '))
    points_list.append(dog_points)

points_list.sort(reverse=True)

max_num = points_list[0]
points_list[0] = points_list[dog - 1]
points_list[dog - 1] = max_num

print('\nРейтинг собак по очкам!\n', points_list, '\nОй! Видимо какая-то ошибка!')
points_list.sort(reverse=True)
print('Минутку\n.\n.\n.\nВот новый рейтинг!\n', points_list)
