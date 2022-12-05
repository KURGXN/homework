shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('\nНазвание детали: ')

detail_info = [0, 0]
for item_index in range(len(shop)):
    if shop[item_index][0] == detail_name:
        detail_info[0] += 1
        detail_info[1] += shop[item_index][1]

print('\nКол-во деталей -', detail_info[0])
print('Общая стоимость -', detail_info[1])
