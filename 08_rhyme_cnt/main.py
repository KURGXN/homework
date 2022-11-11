people_count = int(input('Кол-во человек: '))
rhyming_number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {rhyming_number}-й человек')

people_list = list(range(1, people_count + 1))
begin_number = 0

for _ in range(people_count - 1):
    print('\nТекущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[begin_number])
    people_to_leave = begin_number + rhyming_number - 1
    while people_to_leave >= len(people_list):
        people_to_leave -= len(people_list)
    print('Выбывает человек под номером', people_list[people_to_leave])
    if people_to_leave == len(people_list) - 1:
        begin_number = 0
    else:
        begin_number = people_to_leave
    people_list.remove(people_list[people_to_leave])

print('\nОстался человек под номером', people_list[0])
