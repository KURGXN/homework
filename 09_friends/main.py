friends_count = int(input('Кол-во друзей: '))
iou_number = int(input('Долговых расписок: '))
friends_list = []
for _ in range(friends_count):
    friends_list.append(0)

for iou in range(iou_number):
    print(f'\n{iou + 1}-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[to_whom - 1] -= how_much
    friends_list[from_whom - 1] += how_much

print('\nБаланс друзей:')
for friend in range(friends_count):
    print(f'{friend + 1}:', friends_list[friend])
